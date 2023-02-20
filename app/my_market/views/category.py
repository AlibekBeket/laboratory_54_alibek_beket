from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from my_market.models import *


def category_add_view(request: WSGIRequest):
    if not request.POST:
        return render(request, 'category_add_page.html')
    category_add = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description')
    }
    Category.objects.create(**category_add)
    return redirect(reverse('products_list'))