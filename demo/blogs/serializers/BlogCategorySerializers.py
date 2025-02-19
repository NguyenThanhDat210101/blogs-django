from blogs.models import BlogCategory
from rest_framework import serializers


class BlogCategorySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = BlogCategory
        fields = ['id', 'blog', 'category', 'status']  
        read_only_fields = ['id', 'blog']  