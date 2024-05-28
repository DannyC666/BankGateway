# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('customerHandler/', views.customer_handler, name='customersData'),
    path('customer-products/<str:dni>/', views.query_products, name='query_products'),

]
