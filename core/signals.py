from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def crear_perfil_personalizacion(sender, instance, created, **kwargs):
    
    if instance and created:
        Perfil.objects.update_or_create(user = instance)
        PersonalizacionPerfil.objects.update_or_create(user = instance)