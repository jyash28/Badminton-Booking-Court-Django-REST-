from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_superuser)


class IsAdminAccess(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
