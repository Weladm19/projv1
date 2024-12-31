from django.views.generic import TemplateView


class CarregamentoView(TemplateView):
    template_name = 'escolha.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'carregar carro'
        return context