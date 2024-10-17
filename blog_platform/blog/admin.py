from django.contrib import admin
from .models import BlogPost, Category, Tag

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published_at')
    list_filter = ('category', 'tags')  # Enable filtering by category and tags
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
