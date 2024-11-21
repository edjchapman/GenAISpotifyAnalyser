from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SpotifyAuthView, SpotifyCallbackView, RegisterUser, PasswordResetRequestView, \
    PasswordResetConfirmView, AnalyzeView

urlpatterns = [
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
    path('spotify-auth/', SpotifyAuthView.as_view(), name='spotify_auth'),
    path('callback/', SpotifyCallbackView.as_view(), name='spotify_callback'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
