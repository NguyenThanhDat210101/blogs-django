# blogs/views.py
from blogs.models import Blog
from blogs.serializers.BlogSerializers import BlogSerializer
from helper.helper import dd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import connection, transaction
import logging  

logger = logging.getLogger(__name__)  


@api_view(['GET'])
def my_blog(request):
    return Response({'message': 'my blog!'})


class BlogView(APIView):
    authentication_classes = []
    permission_classes = []

    # API get list blog
    def get(self, request):
        connection.queries.clear() 
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        return Response({"data": serializer.data})

    # API create blog
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BlogByIdView(APIView):
    authentication_classes = []
    permission_classes = []

    # API to get blog by id
    def get(self, request, id):
        try:
            logger.info("start BlogByIdView")  
            blog = Blog.objects.get(id=id)
            logger.debug(f"Found blog: {blog}")
            print("Found blog: ", blog)
            serializer = BlogSerializer(blog)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            logger.error(f"Blog with ID {id} does not exist")  
            return Response(
                {'error': 'Blog not found with this ID'},
                status=status.HTTP_404_NOT_FOUND
            )

    # API to delete blog by id
    def delete(self, request, id):
        try:
            transaction.set_autocommit(False)
            try:
                blog = Blog.objects.get(id=id)
                blog.delete()

                transaction.commit()
                return Response(
                    {'message': f'Blog with ID {id} has been successfully deleted'},
                    status=status.HTTP_200_OK
                )
            except Blog.DoesNotExist:
                transaction.rollback()
                return Response(
                    {'error': 'Blog not found with this ID'},
                    status=status.HTTP_404_NOT_FOUND
                )
        finally:
            transaction.set_autocommit(True)

    # API to update blog by id
    def put(self, request, id):
        try:
            with transaction.atomic():
                blog = Blog.objects.get(id=id)
                serializer = BlogSerializer(blog, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except Blog.DoesNotExist:
            return Response(
                {'error': 'Blog not found with this ID'},
                status=status.HTTP_404_NOT_FOUND
            )
