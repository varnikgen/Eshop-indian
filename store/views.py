from django.http import HttpResponse
from django.shortcuts import render

from .models.category import Category
from .models.product import Product


def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = {'categories': categories, 'products': products, }
    return render(request, 'index.html', data)
