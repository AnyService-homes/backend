from django.db import models
from django.conf import settings

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('waiting_payment', 'Waiting for Payment'),
        ('paid', 'Paid'),
        ('completed', 'Completed'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('visa', 'Visa'),
        ('none', 'None'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer_orders'
    )

    service_man = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='service_man_orders'
    )

    service = models.ForeignKey(
    'services.Service',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='orders'
    )
    booking_time = models.DateTimeField(null=True, blank=True)



    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        default='none'
    )

    payment_status = models.BooleanField(default=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    rating = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"