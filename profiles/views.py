from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

# Create your views here.
class ProfileListView(ListView):

    model = Profile                                 # Modelo de datos que vamos a renderizar
    template_name = 'profiles/profile_list.html'
    # Paginación:
    # paginate_by = 8

