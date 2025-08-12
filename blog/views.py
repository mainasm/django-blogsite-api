from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment, Category, Profile
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, BasePermission

# Create your viewsets here.
    
class IsSuperUser(BasePermission):
  ''' only superusers can access this viewset '''
def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]


class CommentViewSet (viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
