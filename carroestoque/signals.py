from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from carroestoque.models import EstoqueCarroFilipe, EstoqueCarroToninho


@receiver(pre_save , sender=EstoqueCarroFilipe)
def att_valor(sender, instance  , **kwargs):
    produto = instance.produto
    instance.valor = produto.preco_venda
           

@receiver(post_save , sender=EstoqueCarroFilipe)
def att_estoque_produto1(sender, instance , created , **kwargs):
    if created:
        if instance.quantidade > 0:
            produto = instance.produto
            produto.quantidade -= instance.quantidade
            produto.save()    
  
  

@receiver(pre_save , sender=EstoqueCarroToninho)
def att_valor(sender, instance  , **kwargs):
    produto = instance.produto
    instance.valor = produto.preco_venda
                      
  
@receiver(post_save , sender=EstoqueCarroToninho)
def att_estoque_produto2(sender, instance , created , **kwargs):
    if created:
        if instance.quantidade > 0:
            produto = instance.produto
            produto.quantidade -= instance.quantidade
            produto.save()