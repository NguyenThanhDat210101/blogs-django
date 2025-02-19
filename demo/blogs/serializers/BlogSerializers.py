from blogs.serializers.BlogCategorySerializers import BlogCategorySerializer
from blogs.serializers.CategorySerializer import CategorySerializer
from rest_framework import serializers
from ..models import Blog


class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    # categories = BlogCategorySerializer(many=True, read_only=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'categories', 'content', 'created_at', 'updated_at']
