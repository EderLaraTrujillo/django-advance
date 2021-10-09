from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver            # Libreria para hacer los cambios en los datos
from django.db.models.signals import post_save  # Complemento de dispatch

# Función para cargar información tipo media: Imagenes de perfil:
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Función para cargar información tipo media: Imagenes de perfil:
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'galeria/' + filename

# Create your models here.
class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    profesion = models.TextField(verbose_name="Profesion", max_length=120, null=True)
    biografia = models.TextField(verbose_name="Perfil del Usuario", blank=True)
    linkedinUrl = models.URLField(verbose_name='LinkedIn Url', max_length=200, null=True, blank=True)

    # Metadata del Modelo:
    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'
        ordering = ['usuario__username']

# class Photos(models.Model):
#     usuario = models.OneToOneField(User, on_delete=CASCADE)
#     consulta = models.OneToOneField(Albumes, on_delete=CASCADE)
#     imgdiag = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
#     nombFoto = models.TextField(verbose_name="Profesion", max_length=120, null=True)

# class PhotoAlbum(models.Model):
#     usuario = models.OneToOneField(User, on_delete=CASCADE)
#     describe = models.TextField(verbose_name="Profesion", max_length=120, null=True)
#     nombFoto = models.TextField(verbose_name="Profesion", max_length=120, null=True)


# Función exclusiva para los usuarios logueados:
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(usuario=instance)