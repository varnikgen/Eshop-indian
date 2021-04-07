from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Товар')
    image = models.ImageField(upload_to='uploads/category/', null=True, blank=True)

    def __str__(self):
        return self.name
