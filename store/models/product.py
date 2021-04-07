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
