from blogs.models import BlogCategory
from categories.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
         model = Category
         fields = ['id', 'name', 'description', 'status']

    def get_status(self, obj):
        blog_category = BlogCategory.objects.filter(category=obj).first()
        return blog_category.status if blog_category else None

