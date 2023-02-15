from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Item
from .serializers import ItemSerializer
from .permissions import IsItemCreatorOrReadOnly, IsAlgerianResident

class ItemsList(generics.ListAPIView):
   queryset           = Item.objects.filter(is_active=True)
   serializer_class   = ItemSerializer
   permission_classes = (AllowAny,)

class CreateItem(generics.CreateAPIView):
   queryset           = Item.objects.filter(is_active=True)
   serializer_class   = ItemSerializer
   permission_classes = (IsAlgerianResident,)

class ItemDetails(generics.RetrieveUpdateDestroyAPIView):
   queryset = Item.objects.filter(is_active=True)
   serializer_class   = ItemSerializer
   permission_classes = [IsItemCreatorOrReadOnly,]
