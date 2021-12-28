from django.db import models

# Create your models here.
class Shed(models.Model):
    cod = models.IntegerField(default=0)
    capacity = models.FloatField(default=0)
    def __str__(self):
        return self.cod