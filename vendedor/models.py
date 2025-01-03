from django.db import models

from carroestoque.models import EstoqueCarroFilipe

FORMA_DE_PAGAMENTO = {
    'din':'Dinheiro',
    'pix':'Pix',
    'cart':'Cartão',
    'chec':'Cheque',
    'prazo':'Fiado',
}

# Create your models here.
class VenderFilipe(models.Model):
    produto = models.ForeignKey(EstoqueCarroFilipe, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_cliente = models.DecimalField(decimal_places=2,max_digits=7)
    pagamento = models.CharField(choices=FORMA_DE_PAGAMENTO, max_length=20)
    
    
    def __str__(self):
        return self.produto.produto.produto