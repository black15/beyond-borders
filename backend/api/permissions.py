from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsItemCreatorOrReadOnly(BasePermission):
   
   def has_permission(self, request, view):
      if request.user.is_authenticated:
         return True
      return True
      
   def has_object_permission(self, request, view, obj):
      if request.method in SAFE_METHODS:
         return True
      # Instance must have an attribute named `creator`.
      return obj.requester == request.user

class IsAlgerianResident(BasePermission):

   def has_permission(self, request, view):
      if not request.user.is_authenticated:
         return False

      if request.user.user_type == 1:
         return True