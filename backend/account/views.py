from django.shortcuts import render
from rest_framework import generics
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