from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer



def home(request):
    return HttpResponse("Welcome to the BlogSite API")
# Create your viewsets here.
class PostViewSet (viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet (viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






