from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Account

class AccountSerializer(serializers.ModelSerializer):

   class Meta:
      model = Account
      fields = ['email', 'username', 'first_name', 'last_name', 'password', 'phone_number', 'user_type',]
      write_only_fields = ('password',)
      read_only_fields = ('id',)

   def create(self, cd):
      user = Account.objects.create(
         email=cd['email'],
         username=cd['username'],
         first_name=cd['first_name'],
         last_name=cd['last_name'],
         phone_number=cd['phone_number'],
         user_type=cd['user_type']
      )
      
      user.set_password(cd['password'])
      user.save()

      return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['username'] = user.username
        token['user_type'] = user.user_type
        # ...

        return token