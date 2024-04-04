from django.shortcuts import render

#from .cart import Cart
from products.models import Product

#from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def cart_summary(request):
    #cart = Cart(request)
    
    return render(request, 'cart/cart.html')


