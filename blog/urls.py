from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]