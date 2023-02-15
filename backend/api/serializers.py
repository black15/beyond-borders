from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = Item
      read_only_fields = ('slug',)
      fields = ['name', 'slug', 'image', 'description', 'requester', 'category']