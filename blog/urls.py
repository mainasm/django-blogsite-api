from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, PostViewSet, CommentViewSet, ProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


