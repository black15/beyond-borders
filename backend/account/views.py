from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken

from .serializers import AccountSerializer, MyTokenObtainPairSerializer
from .permissions import IsNotAuthenticated

class RegisterView(generics.GenericAPIView):
   
   serializer_class = AccountSerializer
   permission_classes = (IsNotAuthenticated, )

   def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      return Response({
         "user": AccountSerializer(user, context=self.get_serializer_context()).data,
         "message": "User Created Successfully",
      })

class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None
    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken('No valid token found in cookie \'refresh_token\'')

class MyTokenObtainPairView(TokenObtainPairView):
   
   serializer_class = MyTokenObtainPairSerializer

   def post(self, request, *args, **kwargs):
      response = super().post(request, *args, **kwargs)
      token    = response.data["access"]
      refresh  = response.data["refresh"]
      response.set_cookie("access_token", token, httponly=True, max_age=settings.SIMPLE_JWT.get('ACCESS_TOKEN_LIFETIME').total_seconds(), samesite='Lax', secure=False)
      response.set_cookie("refresh_token", refresh, httponly=True)
      return response

class CookieTokenRefreshView(TokenRefreshView):
   def finalize_response(self, request, response, *args, **kwargs):
      if response.data.get('refresh'):
         response.set_cookie('refresh_token', response.data['refresh'], max_age=settings.SIMPLE_JWT.get('REFRESH_TOKEN_LIFETIME'), httponly=True)
         del response.data['refresh']
      return super().finalize_response(request, response, *args, **kwargs)
   serializer_class = CookieTokenRefreshSerializer