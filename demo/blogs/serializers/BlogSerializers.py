from blogs.serializers.BlogCategorySerializers import BlogCategorySerializer
from blogs.serializers.CategorySerializer import CategorySerializer
from categories.models import Category
from django.db import IntegrityError, transaction
from rest_framework import serializers
from ..models import Blog, BlogCategory


class BlogSerializer(serializers.ModelSerializer):
    categories = BlogCategorySerializer(many=True, read_only=False)
    # category_id = serializers.PrimaryKeyRelatedField(
    #     write_only=True,
    #     source='category',
    #     queryset=Category.objects.all(),
    #     required=True
    # )

    class Meta:
        model = Blog
        fields = ['id', 'title', 'categories', 'content', 'created_at']

    def create(self, validated_data):
        try:  
            with transaction.atomic():  
                categories_data = validated_data.pop('categories')
                blog = Blog.objects.create(**validated_data)

                for category_data in categories_data:
                    category, created = Category.objects.get_or_create(
                        id=category_data['category'])
                    BlogCategory.objects.create(
                        blog=blog,
                        category=category,
                        # Default status if not provided
                        status=category_data.get('status', 'active')
                    )
        except IntegrityError as integrityError:
            raise f"Database integrity error during blog creation: {str(integrityError)}"
        except Exception as exception:
            raise serializers.ValidationError(str(exception))
        return blog
