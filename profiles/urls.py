# Importar los paquetes de admin de urls:
from django.urls import path

from registration.models import Profile                         # Admin de Rutas
from .views import ProfileListView                              # Vistas de la aplicación

profiles_patterns = ([
    path('', ProfileListView.as_view(), name = 'Listado'),
], "profiles")
