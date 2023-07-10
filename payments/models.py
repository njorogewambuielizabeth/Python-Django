from django.db import models

# Create your models here.

class Payment(models.Model):
    amount = models.IntegerField()
    order_total = models.IntegerField()
    product_image = models.ImageField(upload_to='payment_images/')
    customer = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment #{self.pk} - {self.customer}"