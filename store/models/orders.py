import datetime
from django.db import models

from .customer import Customer
from .product import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=250, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self) -> str:
        return self.customer.__str__() + " - " + str(self.id)
    