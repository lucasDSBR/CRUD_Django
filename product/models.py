import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    codProd = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    pice = models.FloatField(default=0)
    theAmount = models.IntegerField(default=0)
    manufacturer = models.IntegerField(default=0)
    shed = models.IntegerField(default=0)
    