from django.db.models.signals import post_save
from django.dispatch import receiver

from estoque.models import OutFlow


@receiver(post_save, sender=OutFlow)
def valor(sender,instance,**kwargs):
    print(instance)