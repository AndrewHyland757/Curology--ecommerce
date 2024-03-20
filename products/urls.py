from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('product', views.product, name='product')
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
]