import django
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from store.models.category import Category
from store.models.product import Product


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] -= 1
                else:
                    cart[product] += 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        print('Cart', request.session.get('cart'))

        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        products = None
        categories = Category.get_all_categories()

        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_products_by_categoryID(categoryID)
        else:
            products = Product.get_all_products()

        data = {'categories': categories, 'products': products, }
        return render(request, 'index.html', data)
