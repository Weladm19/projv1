from django.db import models

from area_vendedores.models import VenFilipe


class InforVenda(models.Model):
    produto = models.ForeignKey(VenFilipe, on_delete=models.CASCADE)
    vendedor = models.CharField(max_length=200)
    data_lancamento = models.DateField(auto_now_add=True)
    hora_venda = models.TimeField(auto_now_add=True)
    total_vendido = models.IntegerField()
    
    def __str__(self):
        return f"{self.produto.produto.produto}, {self.vendedor}, {self.data_lancamento}"