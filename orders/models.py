from django.db import models

# Create your models here.
class Order(models.Model):
    order_number = models.IntegerField()
    order_total = models.IntegerField()
    product_image = models.ImageField()
    customer = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)
    product_id = models.IntegerField()
    payment_options = models.CharField(max_length=255)
    order_date = models.DateField()

    def __str__(self):
        return f"Order {self.order_number}"