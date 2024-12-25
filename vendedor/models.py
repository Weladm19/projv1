from django.db import models


# Create your models here.
class Vendedor(models.Model):
    nome = models.CharField(max_length=150)
    salario_fixo = models.DecimalField(max_digits=7, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    obs = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.nome}'
    