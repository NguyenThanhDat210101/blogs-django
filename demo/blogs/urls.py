from django.urls import path
from .views import BlogResouce, BlogByIdResouce, my_blog

urlpatterns = [
    path('', BlogResouce.as_view()),
    path('my-blog', my_blog, name="myBlog"),
    path('<int:id>', BlogByIdResouce.as_view()),
]