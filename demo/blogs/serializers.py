# blogs/serializers.py  
from rest_framework import serializers  
from .models import Blog  
from django.contrib.auth import get_user_model  

User = get_user_model()  

class BlogSerializer(serializers.ModelSerializer):  
    author = serializers.ReadOnlyField(source='author.username')  

    class Meta:  
        model = Blog  
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']  
        read_only_fields = ['author']