from decimal import Decimal

from django.db import models
from django.db.models import Sum

from cliente.models import Cliente
from produto.models import Produto

MODELO_PAGAMENTO = {
    'dinheiro': 'Dinheiro',
    'cartao': 'Cartão',
    'pix': 'Pix',
    'cheque': 'Cheque',
}

class VenLoja(models.Model):
    # vendedor
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2, default=0.00) 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,blank=True , null=True)
    quantidade = models.IntegerField()
    pagamento = models.CharField(max_length=50 ,choices=MODELO_PAGAMENTO )
    obs = models.TextField()
    
    @property
    def total(self):
        tt = self.valor * self.quantidade
        return tt
    

    def __str__(self):
        return f'{self.produto} - {self.cliente} - {self.quantidade} - {self.valor} - {self.pagamento} - {self.obs}'



class VenFilipe(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2) 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,blank=True , null=True)
    quantidade = models.IntegerField()
    pagamento = models.CharField(max_length=50 ,choices=MODELO_PAGAMENTO )
    obs = models.TextField()
    
    @property
    def total(self):
        tt = self.valor * self.quantidade
        return tt
    
    
    @property
    def totalDeTudo(self):
        ver = list(self.tt)
        print(ver)
   
    
    def __str__(self):
        return f'{self.produto} - {self.cliente} - {self.quantidade} - {self.valor} - {self.pagamento} - {self.obs}'
    
    
    
class VenToninho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2) 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,blank=True , null=True)
    quantidade = models.IntegerField()
    pagamento = models.CharField(max_length=50 ,choices=MODELO_PAGAMENTO )
    obs = models.TextField()


    @property
    def total(self):
        tt = self.valor * self.quantidade
        return tt
    
    
    def __str__(self):
        return f'{self.produto} - {self.cliente} - {self.quantidade} - {self.valor} - {self.pagamento} - {self.obs}'