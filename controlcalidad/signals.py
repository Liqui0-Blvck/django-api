from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver


@receiver(post_save, sender=CCRecepcionMateriaPrima)
def comprueba_si_aprueba_cc_por_humedad_recepcionmp(sender, instance, created, **kwargs):
    print(instance.humedad)
    if instance.humedad <= 6:
        CCRecepcionMateriaPrima.objects.filter(pk=instance.pk).update(estado_cc='1')
    else:
        CCRecepcionMateriaPrima.objects.filter(pk=instance.pk).update(estado_cc='0')
    #     