from rest_framework import permissions

class IsYou(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False
        # return obj.username == request.user.username

    def has_permission(self, request, view):
        return False

class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_superuser
        )