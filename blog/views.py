from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

from .models import Post, Comment, Category, Profile
from .serializers import (
    PostSerializer, CommentSerializer, CategorySerializer, ProfileSerializer
)
from .permissions import IsEditorOrReadOnly, IsOwnerOnly

# Posts: only staff/admin can CRUD
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]

# Comments: any authenticated user can CRUD
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

# Categories: everyone authenticated can read; only 'editor' can write
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsEditorOrReadOnly]

# Profiles: each user only sees/edits their own profile
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOnly]

    def get_queryset(self):
        # only their own profile
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
