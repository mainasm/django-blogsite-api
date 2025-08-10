from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, CategoryViewSet, ProfileViewSet

from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)