import os
#import pandas as pd
#import seaborn as sns
import spotipy
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
# load the .env file variables
load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")


kanye_id = 'spotify:artist:5K4W6rqBFWDnAN6FQUkS6x'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
results = spotify.artist_top_tracks(kanye_id)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    #print('audio    : ' + track['preview_url'])
    # print('cover art: ' + track['album']['images'][0]['url'])