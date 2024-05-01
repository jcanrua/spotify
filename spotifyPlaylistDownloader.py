import os
from pytube import YouTube
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch


# Spotify API authentification
clientID = "your_client_ID"
clientSecret = "your_client_secret"
redirectUrl = "https://localhost:8888/callback"  # You can change the port
scope = "playlist-read-private"

sp_auth = SpotifyOAuth(
    client_id=clientID,
    client_secret=clientSecret,
    redirect_uri=redirectUrl,
    scope = scope
)

sp = Spotify(auth_manager=sp_auth)

# Variables 
raw_data = 0
listaFinal = []
urls = []
playlist_url = 0
porcentaje = 0

# Funciones 
def get_playlist():
    resultados = sp.playlist_tracks(playlist_url, None, 100, 0, None)
    raw_data = resultados['items']

    while resultados['next']:
        resultados = sp.next(resultados)
        raw_data.extend(resultados['items'])

    for cancion in raw_data:
        s = VideosSearch(cancion['track']['name'] + ", " + cancion['track']['artists'][0]['name'], limit=1)
        
        link = s.result()['result'][0]['link']
        urls.append(link)
        
        listaFinal.append(cancion['track']['name'] + ", " + cancion['track']['artists'][0]['name'])
        print(cancion['track']['name'] + ", " + cancion['track']['artists'][0]['name'] + " - " + link)

def download():
    yt = YouTube(str(url))  
    video = yt.streams.filter(only_audio=True).first() 

    destination = save_location or '.'
    out_file = video.download(output_path=destination)

    song_name = listaFinal.pop(0)
    new_file = song_name + '.mp3'
    os.rename(out_file, new_file) 
    print(song_name + ": Successfully downloaded.")
    
# Main
if __name__ == "__main__":
    playlist_url = str(input("Enter Spotify playlist URL:\n"))
    save_location = str(input("Enter the destination (blank for current directory):\n"))
    get_playlist()
    print("\nDownloading " + str(len(urls)) + " songs\n")
    for url in urls:
        download()
    print("\nDone\n")
