from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Usuario


class Usuario(models.Model):
    usuario = models.OneToOneField(
        User, verbose_name="usuario", on_delete=models.CASCADE, default=0)
    foto_perfil = models.ImageField(
        upload_to="fotos_perfil", null=True, blank=True, verbose_name="Foto de perfil")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)
