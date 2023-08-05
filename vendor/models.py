from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    account_number = models.CharField(max_length=20)
