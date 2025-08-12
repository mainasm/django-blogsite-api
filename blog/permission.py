from rest_framework.permissions import BasePermission

class CanManagePosts(BasePermission):
    def has_permission(self, request, view):
        return request.user.username == 'caleb'

class CanManageComments(BasePermission):
    def has_permission(self, request, view):
        return request.user.username == 'tom'

class CanManageCategories(BasePermission):
    def has_permission(self, request, view):
        return request.user.username == 'tim'
