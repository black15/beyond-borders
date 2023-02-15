from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsNotAuthenticated(BasePermission):

   def has_permission(self, request, view):
      if not request.user.is_authenticated:
         return True