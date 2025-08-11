from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly, IsEditorOrReadOnly


# Create your viewsets here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsEditorOrReadOnly]