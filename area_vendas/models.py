from django.db import models

from produto.models import Produto
from vendedor.models import Vendedor


# Create your models here.
class EstoqueCarro(models.Model):
    vendedor = models.ForeignKey(Vendedor , on_delete=models.PROTECT)
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_material = models.DecimalField(decimal_places=2, max_digits=7) 
    data_de_adicao = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return f'{self.vendedor}'