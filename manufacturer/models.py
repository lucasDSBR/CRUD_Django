import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Manufacturer(models.Model):
    Manufacturer_Name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.Manufacturer_Name