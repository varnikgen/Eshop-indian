from django.db import models
from .category import Category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/', null=True, blank=True)

    def __str__(self):
        return self.name


    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_products_by_categoryID(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
