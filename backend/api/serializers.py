from rest_framework import serializers
from .models import Item, Category
from account.models import Account

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ('id', 'name', 'slug', 'image',)

class AuthorSerializer(serializers.ModelSerializer):
   author_name = serializers.CharField(source='get_full_name')
   class Meta:
      model = Account
      fields = ['id', 'email', 'username', 'user_type', 'author_name']

class ItemSerializer(serializers.ModelSerializer):
   requester = AuthorSerializer()
   category  = CategorySerializer()

   class Meta:
      model = Item
      read_only_fields = ('slug',)
      fields = ['name', 'slug', 'image', 'description', 'requester', 'category']