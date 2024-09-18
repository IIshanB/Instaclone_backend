from django.contrib.auth import authenticate

from django.contrib.auth.models import Permission
from rest_framework import permissions

class HasLikingPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.has_perm("contents.add_postlikes"):
            return True

        return False