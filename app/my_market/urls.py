from django.urls import path

from my_market.views.products import *
from my_market.views.category import *

urlpatterns = [
    path('', products_view, name='products_list'),
    path('products/', products_view, name='products_list'),
    path('products/add/', product_add_view, name='product_add'),
    path('categories/add/', category_add_view, name='category_add'),
    path('products/<int:pk>', product_view, name='product_detail')
]
