from django.db import models

# Create your models here.
class Shipment(models.Model):
    orders = models.IntegerField()
    customer = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)
    shipment_cost = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Shipment #{self.pk} - {self.customer}"