from django.utils.formats import number_format

from carroestoque.models import EstoqueCarroFilipe, EstoqueCarroToninho


def get_metricas_filipe():
    prod_carro = EstoqueCarroFilipe.objects.all()
    custo_de_estoque = sum(produto.valor * produto.quantidade for produto in prod_carro)
    valor_bruto = sum(produto.valor * produto.quantidade for produto in prod_carro)
    quantidade_total = sum(produto.quantidade for produto in prod_carro)

    
    return dict(
        custo_de_estoque = number_format(custo_de_estoque, decimal_pos=2, force_grouping=True),
        quantidade_total = quantidade_total,
    )
    
    
def get_metricas_toninho():
    prod_carro = EstoqueCarroToninho.objects.all()
    custo_de_estoque = sum(produto.valor * produto.quantidade for produto in prod_carro)
    valor_bruto = sum(produto.valor * produto.quantidade for produto in prod_carro)
    quantidade_total = sum(produto.quantidade for produto in prod_carro)

    
    return dict(
        custo_de_estoque = number_format(custo_de_estoque, decimal_pos=2, force_grouping=True),
        quantidade_total = quantidade_total,
    )