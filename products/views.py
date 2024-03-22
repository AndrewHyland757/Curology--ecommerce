from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404


def index(request):
    """ A view to return the index page """

    all_products = Product.objects.all()
    all_categories = Category.objects.all()

            


    context = {'my_products':all_products, 'my_catagories':all_categories}

    return render(request, 'products/index.html', context)



def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'products/product.html', context)