from django.db import models

# Create your models here.
NIVEL_PAGAMENTO = {
    'BOM': 'bom',
    'MEDIO': 'medio',
    'RUIM': 'ruim',
}

class Cliente(models.Model):
    nome = models.CharField(max_length=150 ,blank=True, null=False)
    acogue = models.CharField(max_length=200)
    cpf_cpnj = models.CharField(max_length=16 ,blank= True, null=True)
    endereco = models.CharField(max_length=100 ,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nivel = models.CharField(max_length=5,choices=NIVEL_PAGAMENTO)
    telefone = models.CharField(max_length=15 ,blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        ordering = ['nome']