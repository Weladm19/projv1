from django.db import models

from produto.models import Produto


class EstoqueCarroFilipe(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(default=0.00 , max_digits=7 , decimal_places=2)
    data_entrada = models.DateTimeField(auto_now_add=True)
    

class EstoqueCarroToninho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(default=0.00 , max_digits=7 , decimal_places=2)
    data_entrada = models.DateTimeField(auto_now_add=True)