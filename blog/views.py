from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment, Category, Profile
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from .permissions import IsEditorOrReadOnly, IsModeratorOrReadOnly, IsStaffOrReadOnly
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsEditorOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsModeratorOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthenticated]  # only logged-in users can access
