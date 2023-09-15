from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        # request bool(request.user and request.user.is_authenticated)

        if request.method in [SAFE_METHODS, 'POST']:
            return True
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in [SAFE_METHODS, 'POST']:
            return True

        if request.user and request.user.is_authenticated and obj.user == request.user:
            return True
        return False

