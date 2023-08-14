from rest_framework.views import Request, View
from rest_framework import permissions
from .models import User

class AdminPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        if request.user.is_superuser or request.user.id == user.id:
            return True