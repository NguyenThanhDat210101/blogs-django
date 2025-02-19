# blogs/views.py
from blogs.models import Blog, BlogCategory
from blogs.serializers.BlogSerializers import BlogSerializer
from categories.models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import connection, transaction
from django.db.models import Prefetch
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
        blogs = Blog.objects.prefetch_related('categories').filter(  
            blogcategory__status='active'  
        ).all()
        serializer = BlogSerializer(blogs, many=True)

        return Response({"data": serializer.data})

    # API create blog
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        # Tạo blog mới
        blog_data = {
            'title': serializer.validated_data['title'],
            'content': serializer.validated_data['content']
        }
        try:
            with transaction.atomic():
                blog = Blog.objects.create(**blog_data)
                blog.save()
                # Tạo các mối quan hệ với category
                categories_data = serializer.validated_data.get(
                    'categories', [])

                # Lấy tất cả các category_id từ categories_data
                category_ids = [category_data.get(
                    'category') for category_data in categories_data]
                # Fetch tất cả các category trong một query duy nhất
                dump(category_ids)
                categories = Category.objects.filter(id__in=category_ids)
                dump(categories)

                # Tạo danh sách các BlogCategory để bulk_create
                blog_categories = []
                for category_data, category in zip(categories_data, categories):
                    print('category_data', category_data)
                    print('category', category)
                    blog_categories.append(BlogCategory(
                        blog=blog,
                        category=category,
                        status=category_data.get('status', 'active')
                    ))

                # Chèn nhiều dòng BlogCategory trong một query
                BlogCategory.objects.bulk_create(blog_categories)

                return Response({
                    'message': 'Blog has been created successfully',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'error exeption': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


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
