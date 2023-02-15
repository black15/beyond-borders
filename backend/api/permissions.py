from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsItemCreatorOrReadOnly(BasePermission):
   
   def has_permission(self, request, view):
      return True
   
   def has_object_permission(self, request, view, obj):
      if request.method in SAFE_METHODS:
         return True
      # Instance must have an attribute named `creator`.
      return obj.requester == request.user
   