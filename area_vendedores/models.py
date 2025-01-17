from django.db import models

from carroestoque.models import EstoqueCarroFilipe, EstoqueCarroToninho


class VenFilipe(models.Model):
    produto = models.ForeignKey(EstoqueCarroFilipe, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True) 
    quantidade = models.IntegerField()
    obs = models.TextField(null=True, blank=True)
   
    class Meta:
       ordering = ['-id']
    
    
    @property
    def total(self):
        tt = self.valor * self.quantidade
        return tt
   
    
    def __str__(self):
        return f'{self.produto} - {self.quantidade} - {self.valor} - {self.obs} - {self.total}'
    
    
class VenToninho(models.Model):
    produto = models.ForeignKey(EstoqueCarroToninho, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True) 
    quantidade = models.IntegerField()
    obs = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        

    @property
    def total(self):
        tt = self.valor * self.quantidade
        return tt
    
    
    def __str__(self):
        return f'{self.produto} - {self.quantidade} - {self.valor} - {self.obs} - {self.total}'
    

# class VenLoja(models.Model):
#     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
#     valor = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, blank=True, null=True) 
#     quantidade = models.IntegerField()
#     obs = models.TextField(null=True, blank=True)
    
#     class Meta:
#        ordering = ['-id']
    
    
#     @property
#     def total(self):
#         tt = self.valor * self.quantidade
#         return tt
    

#     def __str__(self):
#         return f'{self.produto} - {self.quantidade} - {self.valor} - {self.obs} - {self.total}'