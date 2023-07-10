from django.db import models

# Create your models here.
class Notifications(models.Model):
    message = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.message