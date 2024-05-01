# Spotify Playlist Downloader 

This Python script interacts with the Spotify API to download playlists. It downloads the first result that Youtube prompts when searched "song name - artist name" as an .mp3.

# Setup

### 1. Obtain Your Spotify Credentials

To use this script, you'll need to obtain credentials (client ID and client secret) from the Spotify Developer Dashboard:

1. Sign up or log in to your [Spotify Developer account](https://developer.spotify.com/dashboard/).
2. Create a new application and note down the client ID and client secret provided.
3. Set up a redirect URI for your application. This can be any valid URI, by default it should be `http://localhost:8888/callback`. If you use another port, make sure to change it in the code.

### 2. Set Up Credentials

After obtaining your Spotify credentials, go to downloader.py and manually introduce them. If you have changed the redirection URL, make sure to change it also.

### 3. Clone Repository

Clone this repository to your local machine using the following command:

```
git clone https://github.com/jcanrua/spotify-playlist-downloader.git
```

### 4. Install Dependencies

Install the required Python dependencies using pip:

```
pip install -r requirements.txt
```

### 5. Run the Script

You can now run the script using the following command:

```
python3 downloader.py
```

If you plan on using it often, consider making it executable.

## Usage

When executed, it will ask for the playlist URL and the destination folder. Then, it will print "song name, artist name - youtube_url" for every song in the playlist.
After that, it will automatically start downloading.

If you setup your credentials in a .env, it will ask for the redirection URL that opens on your default browser. Depending on the system, it may also do it.


## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

Maybe in the future I will try to make a GUI.
