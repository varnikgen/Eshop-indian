from django.contrib import admin

from .models.category import Category
from .models.product import Product


admin.site.register(Product)
admin.site.register(Category)
