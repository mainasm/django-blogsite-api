from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework import viewsets
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer

# Custom permission example for editor role
class IsEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.username == 'editor'

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.username == 'moderator'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only admin or editor can modify posts
            return [IsAdminUser() | IsEditor()]
        return [IsAuthenticated()]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['destroy']:
            # Only moderator or admin can delete comments
            return [IsAdminUser() | IsModerator()]
        return [IsAuthenticated()]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        # Only admin can modify categories
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
