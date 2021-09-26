from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# Vistas basadas en clases:
class HomePageView(TemplateView):
    # Atributo que indica que template html debe usar:
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
                    'titulo':'Portafolios',
                    'mensaje':'Ten acceso a los perfiles, mas solicitados y preparados del momento.',
                    'pregunta': '¿Qué esperas para empezar?',
                    'boton': 'Registrate!'
                })
