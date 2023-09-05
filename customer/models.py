from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer (models.Model):
    name = models.CharField(max_length=32)
    phone_Number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=32)
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
    
