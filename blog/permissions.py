from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write allowed only to the author or staff
        return obj.author == request.user or request.user.is_staff

class IsEditorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print(f"[DEBUG] Checking permission for user: {request.user.username} and method: {request.method}")
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.username == 'editor'


class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.username == 'moderator'

class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.username == 'staff'