from django.db.models.signals import post_save
from .models import *
from controlcalidad.models  import *
from django.dispatch import receiver



@receiver(post_save, sender=RecepcionMp)
def crear_cc_y_vincular_a_recepcionmp(sender, instance, created, **kwargs):
    if created and instance:
        CCRecepcionMateriaPrima.objects.update_or_create(recepcionmp = instance)
        
