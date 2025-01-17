from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from .models import VenFilipe, VenToninho


@receiver(pre_save, sender=VenFilipe)
def pre_save_ven_filipe(sender, instance, **kwargs):
   produto = instance.produto
   instance.valor = produto.valor


@receiver(pre_save, sender=VenToninho)
def pre_save_ven_toninho(sender, instance, **kwargs):
   produto = instance.produto
   instance.valor = produto.valor
   
   
@receiver(post_save, sender=VenFilipe)
def att_produto(sender , instance, created, **kwargs):
   if created:
     produto = instance.produto
     produto.quantidade -= instance.quantidade
     produto.save()
     
     
@receiver(post_delete, sender=VenFilipe)
def return_valor(sender , instance, **kwargs):
   produto = instance.produto
   produto.quantidade += instance.quantidade
   produto.save()
   
   
@receiver(post_save, sender=VenToninho)
def att_produto_toninho(sender , instance, created, **kwargs):
   if created:
     produto = instance.produto
     produto.quantidade -= instance.quantidade
     produto.save()
     
     
@receiver(post_delete, sender=VenToninho)
def return_valor_toninho(sender , instance, **kwargs):
   produto = instance.produto
   produto.quantidade += instance.quantidade
   produto.save()