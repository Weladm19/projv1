from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OutFlow


@receiver(post_save , sender=OutFlow)
def less_update(sender, instance, created, **kwargs):
    if created:
        if instance.quantidade > 0:
            produto = instance.produto
            produto.quantidade -= instance.quantidade
            produto.save()