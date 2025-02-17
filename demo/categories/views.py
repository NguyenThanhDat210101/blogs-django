# categories/views.py
from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction


class CategoryView(APIView):
    authentication_classes = []
    permission_classes = []

    # API get list category
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response({"data": serializer.data})

    # API create category
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CategoryByIdView(APIView):
    authentication_classes = []
    permission_classes = []

    # API to get category by id
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            print("Found category: ", category)
            serializer = CategorySerializer(category)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(
                {'error': 'Category not found with this ID'},
                status=status.HTTP_404_NOT_FOUND
            )

    # API to delete category by id
    def delete(self, request, id):
        try:
            transaction.set_autocommit(False)
            try:
                category = Category.objects.get(id=id)
                category.delete()

                transaction.commit()
                return Response(
                    {'message': f'Category with ID {id} has been successfully deleted'},
                    status=status.HTTP_200_OK
                )
            except Category.DoesNotExist:
                transaction.rollback()
                return Response(
                    {'error': 'Category not found with this ID'},
                    status=status.HTTP_404_NOT_FOUND
                )
        finally:
            transaction.set_autocommit(True)

    # API to update category by id
    def put(self, request, id):
        try:
            with transaction.atomic():
                category = Category.objects.get(id=id)
                serializer = CategorySerializer(category, data=request.data)

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
        except Category.DoesNotExist:
            return Response(
                {'error': 'Category not found with this ID'},
                status=status.HTTP_404_NOT_FOUND
            )
