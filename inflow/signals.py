from django.db.models.signals import post_save
from django.dispatch import receiver

from inflow.models import InFlow


@receiver(post_save, sender=InFlow)
def update_invetario(sender, instance, created, **kwargs):
    if created:
        if instance.quantidade > 0:
            produto = instance.produto
            produto.quantidade += instance.quantidade
            produto.save()
       
        