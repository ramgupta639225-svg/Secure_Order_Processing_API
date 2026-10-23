from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=80)

    role = models.CharField(
        max_length=20,
        choices=[
            ("admin", "Admin"),
            ("staff", "Staff"),
            ("customer", "Customer"),
        ],
        default="customer",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    