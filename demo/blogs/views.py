# blogs/views.py
from demo.blogs.forms.createBlogForm import createBlogFrom
from demo.blogs.models import Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view(['GET'])
def my_blog(request):
    return Response({'message': 'my blog!'})

class BlogResouce(APIView):
    authentication_classes = []
    permission_classes = []

    # API get list blog
    def get(self, request):
        # result = Blog.objects.all()
        return Response({'data': "hihi"})

    # API create blog
    # def post(self, request):
        # form = createBlogFrom(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return Response({'message': 'Blog created!'})
        # else:
        #     return Response({'message': 'Error!'})

class BlogByIdResouce(APIView):
    authentication_classes = []
    permission_classes = []

    # API get blog by id
    def get(self, request, id):
        return Response({'message': 'detail blog by id: ' + str(id)})

    # API delete blog by id
    def delete(self, request, id):
        return Response({'message': 'delete blog by id: ' + str(id)})

    # API update blog by id
    def put(self, request, id):
        return Response({'message': 'Get blog by id: ' + str(id)})
