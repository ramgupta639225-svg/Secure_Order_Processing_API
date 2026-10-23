from django.db import models

# Create your models here.
from django.db.models import Q
from products.models import Product

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='inventory',)
    quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.name} -Stock:  {self.quantiity}'