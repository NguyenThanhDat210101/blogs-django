# from blogs.serializers import BlogSerializer
# from blogs.serializers import BlogSerializer
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):  
    # blogs = BlogSerializer(many=True, read_only=True, required=False)  

    class Meta:  
        model = Category  
        fields = ['id', 'name', 'description', 'blogs']  # Include 'blogs' here by default  

    def to_representation(self, instance):  
        representation = super().to_representation(instance)  
        
        # Check context for controlling visibility of 'blogs'  
        if self.context.get('exclude_blogs', False):  
            representation.pop('blogs', None)  # Remove 'blogs' field if context says to exclude  
        
        return representation  
