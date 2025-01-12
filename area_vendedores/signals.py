from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import VenFilipe


@receiver(pre_save, sender=VenFilipe)
def pre_save_ven_filipe(sender, instance, **kwargs):
   produto = instance.produto
   instance.valor = produto.preco_venda
   
