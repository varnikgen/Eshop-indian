from store.models.customer import Customer
from django.contrib import admin

from .models.category import Category
from .models.product import Product
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'image']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
