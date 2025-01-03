from django.db import models
from django.utils.formats import number_format

from produto.models import Produto


class EstoqueCarroFilipe(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=7 , decimal_places=2, blank=True, null=True ,default=0.00) 
    data_entrada = models.DateTimeField(auto_now_add=True)
    
    @property
    def total_valor(self):
        total = self.quantidade * self.valor
    
        return number_format(total , force_grouping=True, decimal_pos=2 )
    
    
    def __str__(self):
        return f'{self.produto}'
    
class EstoqueCarroToninho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=7 , decimal_places=2, blank=True, null=True ,default=0.00)
    data_entrada = models.DateTimeField(auto_now_add=True)
    
    @property
    def total_valor(self):
        total = self.quantidade * self.valor
    
        return number_format(total , force_grouping=True, decimal_pos=2 )
    
    
    def __str__(self):
        return f'{self.produto}'