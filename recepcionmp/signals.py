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
        
        print(instance)
        
        # Lógica para generar el número de lote
        year = datetime.now().year
        ultimo_numero_lote = RecepcionMp.objects.filter(numero_lote__contains=str(year)).order_by('-numero_lote').first()
        if ultimo_numero_lote:
            numero_anterior = int(ultimo_numero_lote.numero_lote.split('-')[0])
            nuevo_numero = numero_anterior + 1
        else:
            nuevo_numero = 1
        nuevo_numero_lote = f"{nuevo_numero:02d}-{year}"
        instance.numero_lote = nuevo_numero_lote
        instance.save()