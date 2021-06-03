from django.urls import path
from .middlewares.auth import auth_middleware

from .views.cart import Cart
from .views.checkout import Checkout
from .views.login import Login, logout
from .views.orders import OrderView
from .views.signup import Signup
from .views.home import Index


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('cart', Cart.as_view(), name='cart'),
    path('logout', logout, name='logout'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
