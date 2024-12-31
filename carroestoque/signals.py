from django.db.models.signals import post_save
from django.dispatch import receiver

from carroestoque.models import EstoqueCarroFilipe, EstoqueCarroToninho


@receiver(post_save , sender=EstoqueCarroFilipe)
def att_estoque_produto1(sender, instance , created , **kwargs):
    if created:
        if instance.quantidade > 0:
            produto = instance.produto
            produto.quantidade -= instance.quantidade
            produto.save()
            
            

@receiver(post_save , sender=EstoqueCarroToninho)
def att_estoque_produto2(sender, instance , created , **kwargs):
    if created:
        if instance.quantidade > 0:
            produto = instance.produto
            produto.quantidade -= instance.quantidade
            produto.save()