from django.urls import path

from .views.login import Login
from .views.signup import Signup
from .views.home import Index


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
]
