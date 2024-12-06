from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('farmer/register/', views.farmer_register, name='farmer_register'),
    path('customer/register/', views.customer_register, name='customer_register'),
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('customer/dashboard/', views.customer_dashboard, name='customer_dashboard'),
]