from store.models.product import Product
from django.contrib.auth.hashers import check_password
from django.views import View
from django.shortcuts import redirect, render

from store.models.customer import Customer
from store.models.product import Product


class Cart(View):
    def get(self, request):
        ids =list(request.session['cart'].keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})
