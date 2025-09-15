from django.db import models

class TransportOrder(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.order_number} - {self.customer_name}"

    @property
    def waypoints_count(self):
        return self.waypoints.count()

class Waypoint(models.Model):
    TYPE_CHOICES = [
        ('Pickup', 'Pickup'),
        ('Delivery', 'Delivery'),
    ]
    order = models.ForeignKey(
        TransportOrder,
        related_name='waypoints',
        on_delete=models.CASCADE
    )
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.type} - {self.location}"
