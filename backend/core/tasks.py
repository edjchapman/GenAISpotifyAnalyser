from celery import shared_task
from .spotify_helper import get_spotify_client
from .models import SpotifyData
from django.contrib.auth.models import User

@shared_task
def fetch_spotify_data(user_id):
    user = User.objects.get(id=user_id)
    token_info = user.session.get('token_info')
    if not token_info:
        return "No token available"

    sp = get_spotify_client(token_info)
    top_tracks = sp.current_user_top_tracks(limit=10)
    saved_tracks = sp.current_user_saved_tracks(limit=10)

    spotify_data, created = SpotifyData.objects.get_or_create(user=user)
    spotify_data.top_tracks = top_tracks
    spotify_data.saved_tracks = saved_tracks
    spotify_data.save()

    return "Data fetched successfully"
