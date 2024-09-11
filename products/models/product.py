from django.db import models
from django.utils import timezone
from shared.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


# Restaurant model
class Restaurant(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    contact_email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


    def __str__(self):
        return self.name


# Category model
class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.name


# MenuItem model
class MenuItem(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('archived', 'Archived'),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='menu_items')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    stock = models.IntegerField(default=1)


    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.stock > 0

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            return False

        self.stock -= quantity
        self.save()
        return True

    def increase_stock(self, amount):
        self.stock += amount
        self.save()

    class Meta:
        ordering = ['name']


