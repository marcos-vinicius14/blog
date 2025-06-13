from rest_framework import serializers
from .models import Post, Category, Tag
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = ['id', 'username', 'first_name', 'last_name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fiels = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        author = UserSerializer(read_only=True)
        category = CategorySerializer()
        tags = TagSerializer(many=True)

        class Meta:
            model = Post
            fields = ['id', 'title', 'content', 'author', 'tags', 'published_at']