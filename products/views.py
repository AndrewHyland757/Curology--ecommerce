from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404


def index(request):
    """ A view to return the index page """

    all_products = Product.objects.all()
    context = {'my_products':all_products}

    return render(request, 'products/index.html', context)





def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}
