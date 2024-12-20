from django.shortcuts import redirect
from django.views.generic import TemplateView

class ViewHome(TemplateView):
    template_name = 'index.html'