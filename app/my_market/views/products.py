from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from my_market.models import *


def products_view(request: WSGIRequest):
    return render(request, 'products_list_page.html')

