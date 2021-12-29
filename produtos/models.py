from django.db import models

# Create your models here.

class Produtos(models.Model):
    prod_Nome = models.CharField(max_length=200)
    prod_Codigo = models.IntegerField(default=0)
    prod_Preco = models.FloatField(default=0)
    prod_Total_estoque = models.IntegerField(default=0)
    prod_Fornecedor = models.IntegerField(default=0)
    def __str__(self):
        return self.prod_Nome