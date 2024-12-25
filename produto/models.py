from django.db import models


# Create your models here.
class Tipo(models.Model):
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.tipo}"


class Produto(models.Model):
    produto = models.CharField(max_length=200)
    tipo = models.OneToOneField(Tipo, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    custo = models.DecimalField(decimal_places=2 , max_digits=8)
    preco_venda = models.DecimalField(decimal_places=2 , max_digits=8)
    quantidade = models.IntegerField()
    
    def __str__(self):
        return f"{self.produto}"