from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from my_market.models import *


def products_view(request: WSGIRequest):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list
    }
    return render(request, 'products_list_page.html', context=context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_print_page.html', context={
        'product': product,
    })


def product_add_view(request: WSGIRequest):
    if not request.POST:
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'product_add_page.html', context=context)
    categories = Category.objects.all()
    for category in categories:
        if category.title == request.POST.get('category'):
            product_category = category
    product_add = {
        'title': request.POST.get('title'),
        'price': request.POST.get('price'),
        'picture': request.POST.get('url_picture'),
        'category': product_category,
        'description': request.POST.get('description')
    }
    product = Product.objects.create(**product_add)
    print(product.pk)
    return redirect('/products/' + str(product.pk))
