from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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