import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Employees(models.Model):
    Employee_Name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=10)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length= 20)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.Employee_Name 