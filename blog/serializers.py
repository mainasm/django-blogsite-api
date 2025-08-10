# Import serializers class from rest_framework
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
# Import the models to serialize
from .models import Post, Comment, Category, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)  # Make author read-only


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# If you have a Profile model, you can add its serializer here as well

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar']
        read_only_fields = ['id', 'user']