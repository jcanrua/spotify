import youtube_dl
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch

########## Spotify API authentification ##########

clientID = "a7bf021e80114e5ebecf982370aaf17e"
clientSecret = "2e4a96c283394ee7b2d4e50aaf26316a"
redirectUrl = "https://localhost:8888/callback"
scope = "playlist-read-private"

sp_auth = SpotifyOAuth(
    client_id=clientID,
    client_secret=clientSecret,
    redirect_uri=redirectUrl,
    scope = scope,
)

sp = Spotify(auth_manager=sp_auth)


############   Youtube_dl parameters  ############

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': f'%(title)s.%(ext)s',
}


#################### Variables ####################

raw_data = 0
listaFinal = []
urls = []
playlist_url = 0
porcentaje = 0

#################### Funciones ####################

def get_playlist():
    global raw_data, listaFinal, urls

    resultados = sp.playlist_tracks(playlist_url, None, 100, 0, None)
    raw_data = resultados['items']

    while resultados['next']:
        resultados = sp.next(resultados)
        raw_data.extend(resultados['items'])

    for cancion in raw_data:
        s = VideosSearch(cancion['track']['name'] + ", " + cancion['track']['artists'][0]['name'], limit=1)
        link = s.result()['result'][0]['link']
        urls.append(link)
        listaFinal.append(cancion['track']['name'] + " - " + cancion['track']['artists'][0]['name'])
        
        #print(cancion['track']['name'] + ", " + cancion['track']['artists'][0]['name'] + " - " + link)


def download():
    global urls, ydl_opts
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)
        porcentaje = porcentaje + (len(urls)/100)
