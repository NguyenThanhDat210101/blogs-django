from django import form

from demo.blogs.models import Blog


class createBlogFrom(form.Form):
    class Meta:
        model: Blog
        field = ['title', 'content']