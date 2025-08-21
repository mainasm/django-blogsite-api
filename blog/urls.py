from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, CategoryViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]