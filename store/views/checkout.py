from store.models.product import Product
from django.contrib.auth.hashers import check_password
from django.views import View
from django.shortcuts import redirect, render

from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, products)

        for product in products:
            order = Order(customer=Customer(id=customer), product=product, price=product.price,
                          address=address, phone=phone, quantity=cart.get(str(product.id)))
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('cart')
