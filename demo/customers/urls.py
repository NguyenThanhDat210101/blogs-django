from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_customer, name='create_customer'),
    path('', views.customer_list, name='customer_list'),
]