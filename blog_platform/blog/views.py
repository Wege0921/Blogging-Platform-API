# blog/views.py
from rest_framework import generics, permissions
from .models import BlogPost, Category, Tag
from .serializers import BlogPostSerializer, CategorySerializer, TagSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Only allow the author to update the post
        if self.request.user == self.get_object().author:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to edit this post.")

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
