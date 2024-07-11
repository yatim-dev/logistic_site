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
    uuid = models.CharField(max_length=22, unique=True, default=shortuuid.uuid)
    start_city = models.CharField(max_length=255)
    end_city = models.CharField(max_length=255)
    current_city = models.CharField(max_length=255)
    create_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.uuid}"


class UserInput(models.Model):
    string = models.CharField(max_length=22)

    def __str__(self):
        return self.string


class Support(models.Model):
    email = models.CharField(max_length=50)
    order_id = models.CharField(max_length=22)
    title = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.title