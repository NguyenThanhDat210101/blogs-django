from blogs.models import BlogCategory
from rest_framework import serializers


class BlogCategorySerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=False)
    class Meta:
        model = BlogCategory
        fields = ['id', 'status']
        read_only_fields = ['id']

