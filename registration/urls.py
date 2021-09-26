''' 
    Archivo de configuración de urls
    para el registro del usuario: app-registration
'''
# Importar los paquetes de admin de urls:
from django.urls import path                        # Admin de Rutas
from django.urls.resolvers import URLPattern        # Resuelve las Rutas
from .views import SingUpView, ProfileUpdate        # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('singup/', SingUpView.as_view(), name="singup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
 ]