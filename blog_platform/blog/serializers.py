from rest_framework import serializers
from .models import BlogPost, Category, Tag
from users.models import CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Display author as string
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), source='tags', write_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'category_id', 'tags', 'tag_ids', 'created_at', 'published_at']

