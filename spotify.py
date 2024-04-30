import youtube_dl
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch

clientID = "a7bf021e80114e5ebecf982370aaf17e"
clientSecret = "2e4a96c283394ee7b2d4e50aaf26316a"
redirectUrl = "https://localhost:8888/callback"
scope = "playlist-read-private"

sp_auth = SpotifyOAuth(
    client_id=clientID,
    client_secret=clientSecret,
    redirect_uri=redirectUrl,
    scope = scope,
    show_dialog=True
)

sp = Spotify(auth_manager=sp_auth)

resultados = sp.playlist_tracks(
    "https://open.spotify.com/playlist/3jH3pkKUTAR4XCUMks2l4z",
    None, 100, 0, None)

raw_data = resultados['items']
while resultados['next']:
    resultados = sp.next(resultados)
    raw_data.extend(resultados['items'])

listaFinal = []
urls = []
for cancion in raw_data:
    s = VideosSearch(cancion['track']['name'] + ", " + cancion['track']['artists'][0]['name'], limit=1)
    link = s.result()['result'][0]['link']
    listaFinal.append(cancion['track']['name'] + " - " + cancion['track']['artists'][0]['name'])
    urls.append(link)
    #print(cancion['track']['name'] + ", " + cancion['track']['artists'][0]['name'] + " - " + link)


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': f'%(title)s.%(ext)s',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)
