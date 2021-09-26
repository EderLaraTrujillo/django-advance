from django.urls import path
# Importar las vistas:
from .views import HomePageView

urlpatterns = [
   path('', HomePageView.as_view(), name='inicio')
]
