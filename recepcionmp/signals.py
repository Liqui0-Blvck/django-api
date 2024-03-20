from django.db.models.signals import post_save, pre_save
from .models import *
from controlcalidad.models  import *
from django.dispatch import receiver
from datetime import datetime



@receiver(post_save, sender=RecepcionMp)
def crear_cc_y_generar_numero_lote(sender, instance, created, **kwargs):
    if created and instance:
        # Lógica para crear CCRecepcionMateriaPrima
        CCRecepcionMateriaPrima.objects.update_or_create(recepcionmp=instance)
        
        
        ultimo_numero_lote = RecepcionMp.objects.exclude(numero_lote__isnull=True).order_by('-numero_lote').first()
        if ultimo_numero_lote:
            nuevo_numero = ultimo_numero_lote.numero_lote + 1
        else:   
            nuevo_numero = 1  # Si no hay números de lote, comienza desde 1
        # Asigna el nuevo número de lote al objeto actual
        instance.numero_lote = nuevo_numero
        # Guarda el objeto con el nuevo número de lote
        instance.save()