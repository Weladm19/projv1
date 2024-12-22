from django.db import models

from produto.models import Produto


# Create your models here.
class InFlow(models.Model):
    tipo_in = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_pro = models.IntegerField()
    
class OutFlow(models.Model):
    tipo_ou = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_pro = models.IntegerField()