from django.db import models

from produto.models import Produto


# Create your models here.
class InFlow(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_lancamento = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['produto']
        
    def __str__(self):
        return self.produto.produto