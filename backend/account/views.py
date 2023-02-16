from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

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

class MyTokenObtainPairView(TokenObtainPairView):
   
   serializer_class = MyTokenObtainPairSerializer

   def post(self, request, *args, **kwargs):
      response = super().post(request, *args, **kwargs)
      token = response.data["access"]
      response.set_cookie("account_token", token, httponly=True)
      return response