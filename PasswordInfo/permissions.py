from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
     """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an user attribute.
    """

     def has_object_permission(self,request,view,obj):
          return obj.user == request.user