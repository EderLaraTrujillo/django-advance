''' 
    Archivo de configuración de urls
    para el registro del usuario: app-registration
'''
# Importar los paquetes de admin de urls:
from django.urls import path                        # Admin de Rutas
from django.urls.resolvers import URLPattern        # Resuelve las Rutas
from .views import SingUpView                       # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('singup/', SingUpView.as_view(), name="singup")
 ]