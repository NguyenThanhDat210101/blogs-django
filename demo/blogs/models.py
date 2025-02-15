# blogs/models.py  
from django.db import models  
from django.contrib.auth import get_user_model  

class Blog(models.Model):  
    title = models.CharField(max_length=255)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'blogs'