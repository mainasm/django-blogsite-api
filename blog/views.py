from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment, Category, Profile
from .serializers import PostSerializer, CommentSerializer, CategorySerializer , ProfileSerializer
from rest_framework.permissions import SAFE_METHODS

# Custom permissions
class IsOwnerOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'user'):
            return obj.user == request.user or request.user.is_staff
        return False

class IsAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_staff)
        )

# Create your viewsets here.
class PostViewSet (viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrStaff]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet (viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrStaff]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def get_queryset(self):
        """Restrict queryset to user's own profile (or all for staff)"""
        user = self.request.user
        if user.is_staff:
            return Profile.objects.all()
        return Profile.objects.filter(user=user)

    def perform_create(self, serializer):
        """Automatically assign profile to current user"""
        serializer.save(user=self.request.user)