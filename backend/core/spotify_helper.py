from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def get_spotify_oauth():
    return SpotifyOAuth(
        client_id='your-client-id',
        client_secret='your-client-secret',
        redirect_uri='http://localhost:8000/api/callback',
        scope="user-top-read user-library-read",
    )

def get_spotify_client(token_info):
    return Spotify(auth=token_info['access_token'])
