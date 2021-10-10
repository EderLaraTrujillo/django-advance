# Importar los paquetes de admin de urls:
from django.urls import path

from registration.models import Profile                         # Admin de Rutas
from .views import ProfileListView, ProfileDetailView           # Vistas de la aplicación

profiles_patterns = ([
    path('', ProfileListView.as_view(), name = 'listado'),
    path('<username>/', ProfileDetailView.as_view(), name = 'perfil'),
], "profiles")
