from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the object.
        return obj.author == request.user

class IsEditorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the 'editor' user to create or edit.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.username == 'editor'