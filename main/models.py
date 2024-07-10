import shortuuid
from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('on_way', 'On Way'),
        ('delivered', 'Delivered'),
        ('issued', 'Issued'),
    ]

    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=22, unique=True, editable=False, default=shortuuid.uuid)
    start_city = models.CharField(max_length=255)
    end_city = models.CharField(max_length=255)
    current_city = models.CharField(max_length=255)
    create_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.uuid}"
