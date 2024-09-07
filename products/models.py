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


    def __str__(self):
        return self.name


# Order model
class Order(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('archived', 'Archived'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order by {self.customer}"


# OrderItem model
class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.menu_item.name}"


# Payment model
class Payment(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]


    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    transaction_id = models.CharField(max_length=255)


    def __str__(self):
        return f"Payment for order {self.order}"