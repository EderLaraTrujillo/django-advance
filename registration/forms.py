from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from .models import Profile

# Formulario para validar email ya registrado::
class UserCreationWithEmail(UserCreationForm):
    # 1. Capturamos el correo desde el formulario:
    email = forms.EmailField(required=True, help_text="Requerido, 200 caracteres como máximo")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password1")

    # 2. Validamos si el usuario existe en la base de datos:
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email= email).exists():
            raise forms.ValidationError("El Email ya se encuentra registrado.")
        return email
    # Fin

# Clase para el formulario de mi perfil como usuario:
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','profesion','biografia','linkedinUrl']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
            'profesion': forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Profesión u Ocupación'}),
            'biografia': forms.Textarea(attrs = {'class':'form-control mt-2', 'placeholder':'Biografia y/o Perfil Ocupacional', 'rows':'9'}),
            'linkedinUrl': forms.URLInput(attrs = {'class':'form-control mt-2', 'placeholder':'LinkedIn Url'}),
        }

