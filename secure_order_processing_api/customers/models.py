from django.db import models

# Create your models here.
from django.con import setting

class Customer(models.Model):
    user = models.OneToOneField(setting.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_profile',)
    phone = models.CharField(max_length=13, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    