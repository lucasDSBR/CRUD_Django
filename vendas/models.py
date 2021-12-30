from django.db import models

# Create your models here.


class Vendas(models.Model):
    venda_Cod = models.IntegerField(default=0)
    venda_Data = models.DateTimeField(default='00/00/0000 00:00:00')
    venda_Cliente = models.IntegerField(default=0)
    venda_Prod = models.IntegerField(default=0)
    venda_Metodo_Pagamento = models.IntegerField(default=0)
    venda_estado_destino = models.CharField(max_length=10)
    venda_quantidade_produto = models.IntegerField(default=0)
    venda_total = models.FloatField(default=0.0)
    def __str__(self):
        return self.venda_Cod