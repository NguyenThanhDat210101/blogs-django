from categories.models import Category
from categories.serializers.BlogSerializers import BlogSerializer
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'blogs']
