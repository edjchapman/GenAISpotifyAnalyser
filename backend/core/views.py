from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.spotify_helper import get_spotify_oauth
from .tasks import fetch_spotify_data


class SpotifyAuthView(APIView):
    def get(self, request):
        sp_oauth = get_spotify_oauth()
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

class SpotifyCallbackView(APIView):
    def get(self, request):
        sp_oauth = get_spotify_oauth()
        code = request.GET.get('code')
        token_info = sp_oauth.get_access_token(code)
        request.session['token_info'] = token_info
        user = request.user
        fetch_spotify_data.delay(user.id)  # Schedule task to fetch data
        return Response({'message': 'Authentication successful'})

class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = f"http://localhost:3000/reset-password/{uid}/{token}"
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_url}',
                'your-email@gmail.com',
                [email],
            )
        return Response({'message': 'If the email exists, a reset link has been sent.'})

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if not default_token_generator.check_token(user, token):
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

            password = request.data.get('password')
            user.set_password(password)
            user.save()
            return Response({'message': 'Password reset successful.'})
        except (User.DoesNotExist, ValueError, TypeError):
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

class AnalyzeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Dummy data for now, you can replace it with actual Spotify analysis
        data = {
            'top_genres': {'rock': 5, 'pop': 3, 'jazz': 2},
            'top_tracks': ['Track 1', 'Track 2', 'Track 3']
        }
        return Response(data)