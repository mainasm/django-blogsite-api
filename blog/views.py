from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permission import IsAuthorOrReadOnly


# Create your viewsets here.
class PostViewSet (viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class CommentViewSet (viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
