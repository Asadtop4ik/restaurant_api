from django.db import models
from django.contrib.auth import get_user_model
from shared.models import BaseModel
from .product import Restaurant, MenuItem

User = get_user_model()

# Order model
class Order(BaseModel):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    is_paid = models.BooleanField(default=False, null=True)

    def set_status(self, new_status):
        if new_status not in dict(self.STATUS_CHOICES):
            raise ValueError("Invalid status")
        self.status = new_status
        self.save()

    def is_transition_allowed(self, new_status):
        allowed_transitions = {
            self.PENDING: [self.PROCESSING, self.CANCELED],
            self.PROCESSING: [self.SHIPPED, self.CANCELED],
            self.SHIPPED: [self.COMPLETED, self.CANCELED],
        }

        return new_status in allowed_transitions.get(self.status, [])

    def __str__(self):
        return f"Order by {self.customer} for {self.restaurant}"


# Payment model
class Payment(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255)


    def __str__(self):
        return f"Payment for order {self.order}"