from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsEditorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            (request.user.is_authenticated and request.user.username == 'editor')
        )

class IsModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            (request.user.is_authenticated and request.user.username == 'moderator')
        )

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            (request.user.is_authenticated and request.user.username == 'staff')
        )
