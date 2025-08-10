from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsEditorOrReadOnly(BasePermission):
    """
    Authenticated users can read.
    Only users with the username 'editor' can write.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # write actions
        return request.user and request.user.is_authenticated and request.user.username == "editor"


class IsOwnerOnly(BasePermission):
    """
    Only the owner can access the profile endpoint.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

    def has_permission(self, request, view):
        # must be logged in to even hit the route
        return request.user and request.user.is_authenticated
