from rest_framework import serializers
from .models import Blog
from categories.serializers import CategorySerializer
from categories.models import Category

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='category',
        queryset=Category.objects.all(),
        required=True
    )

    class Meta:
        model = Blog
        fields = ['id', 'title', 'category',
                  'category_id', 'content', 'created_at']
