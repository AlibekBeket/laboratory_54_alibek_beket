from django.contrib import admin

from my_market.models import *


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "category", "created_at", "picture")
    list_filter = ("id", "title", "category", "description", "price", "created_at")
    search_fields = ("id", "title", "description", "price", "category", "picture")
    fields = ("title", "description", "price", "category", "created_at", "picture")
    readonly_fields = ("id", "created_at")


admin.site.register(Products, ProductsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_filter = ("id", "title", "description")
    search_fields = ("id", "title", "description")
    fields = ("title", "description")


admin.site.register(Category, CategoryAdmin)
