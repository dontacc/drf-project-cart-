from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or \
            request.user.is_superuser:
            return True



class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS :
            return True

        bool (request.user and request.is_staff)



