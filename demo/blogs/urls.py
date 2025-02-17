from django.urls import path
from .views import BlogView, BlogByIdView, my_blog

urlpatterns = [
    path('', BlogView.as_view()),
    path('my-blog', my_blog, name="myBlog"),
    path('<int:id>', BlogByIdView.as_view()),
]