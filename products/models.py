import datetime
from django.db import models
from django.utils import timezone
from manufacturer import Manufacturer
from shed import Shed
# Create your models here.
class Products(models.Model):
    Product_Name = models.CharField(max_length=200)
    cod = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    total = models.IntegerField(default=0)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    shed = models.ForeignKey(Shed, on_delete=models.CASCADE)
    def __str__(self):
        return self.Product_Name