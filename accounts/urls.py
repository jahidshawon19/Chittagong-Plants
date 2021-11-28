from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('customers/', views.allCustomer, name="customers"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('upate_customer/<str:pk>/',views.updateCustomer,name="update-customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer,name="delete-customer"),

    path('categories/', views.category,name="categories"),
    path('create_cat/', views.createCategory, name="create_category"),
    path('update_cat/<str:pk>/', views.updateCategory,name="update-category"), 
    path('delete_cat/<str:pk>/', views.deleteCategory,name="delete-category"),   

    path('products/', views.product, name="products"),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct,name="update-product"),
    path('delete_product/<str:pk>/', views.deleteProduct,name="delete-product"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]