from django.urls import path
from .views import CategoryView, CategoryByIdView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('<int:id>', CategoryByIdView.as_view()),
]