from django.db import models
from django.contrib.auth.models import User

class SpotifyData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    top_tracks = models.JSONField()
    saved_tracks = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)
