from django.http import HttpResponse
from django.shortcuts import render

from .models.category import Category
from .models.product import Product


def index(request):
    products = None
    categories = Category.get_all_categories()
    
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_products_by_categoryID(categoryID)
    else: 
        products = Product.get_all_products()

    data = {'categories': categories, 'products': products, }
    return render(request, 'index.html', data)


def signup(request):
    return render(request, 'signup.html')
