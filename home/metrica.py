from django.utils.formats import number_format

from produto.models import Produto


def get_metricas():
    produto_total = Produto.objects.all()
    custo_de_estoque = sum(produto.custo * produto.quantidade for produto in produto_total)
    valor_bruto = sum(produto.preco_venda * produto.quantidade for produto in produto_total)
    valor_liquido = valor_bruto - custo_de_estoque 
    quantidade_total = sum(produto.quantidade for produto in produto_total)
    lucro = (float(valor_liquido) * 0.30)
    
    return dict(
        custo_de_estoque = number_format(custo_de_estoque, decimal_pos=2, force_grouping=True),
        valor_bruto = number_format(valor_bruto, decimal_pos=2, force_grouping=True),
        valor_liquido = number_format(valor_liquido, decimal_pos=2, force_grouping=True),
        quantidade_total = quantidade_total,
        lucro = number_format(lucro, decimal_pos=2, force_grouping=True)
    )