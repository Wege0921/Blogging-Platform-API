# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.BlogPostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.BlogPostDetailView.as_view(), name='post-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('tags/', views.TagListView.as_view(), name='tag-list'),
]
