from django.db import models

# Create your models here.
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator

class Order(models.Model):
    class Status(models.TextChoices):

        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'

        customer = models.ForeignKey("customers.Customer", on_delete=models.PROTECT, related_name="orders",)
        status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING,)
        total_amount = models.DecimalField(max_length=12, decimal_places=2, default=Decimal("0.00"), validators=[MinValueValidator(Decimal("0.00"))],)

        created_at = models.DecimalField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)




class OrderItem(models.Model):

    order = models.ForeignKey("Order", on_delete=CASCADE, related_name='items',)
    prodect = models.ForeignKey("products.Product", on_delete=models.PROTECT, related_name='order_item',)

    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)],)

    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))],)

    created_at =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order  #{self.order_id} {self.product.name}"