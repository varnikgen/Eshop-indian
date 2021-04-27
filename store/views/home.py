from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from store.models.category import Category
from store.models.product import Product


print(make_password('123'))


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