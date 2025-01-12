from django.utils.formats import number_format

from .models import VenFilipe


def metrica_vendedor():
    resultado = 0.00
    for i in VenFilipe.objects.all():
        resultado +=  float(i.total)
    return dict(
        valorTotal = number_format(resultado, decimal_pos=2 , force_grouping=True),
    )