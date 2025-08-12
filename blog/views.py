from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer

# === Custom Permissions ===
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

# === ViewSets ===
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, CanManagePosts]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CanManageComments]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, CanManageCategories]
