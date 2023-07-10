from django.db import models

# Create your models here.
class Review(models.Model):
    message = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    number_of_stars = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Review #{self.pk} - {self.customer} - {self.product}"