from blogs.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'title','content', 'created_at']
