from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from account.views import RegisterView, MyTokenObtainPairView, CookieTokenRefreshView

app_name = 'account'

urlpatterns = [
    path('signin/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('signup/', RegisterView.as_view(), name='register'),
]