from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from recepcionmp.models import RecepcionMp, GuiaRecepcionMP


@receiver(post_save, sender=CCRecepcionMateriaPrima)
def comprueba_si_aprueba_cc_por_humedad_recepcionmp(sender, instance, created, **kwargs):
    print(instance.humedad)
    if instance and created:
        pass
    else:
        if instance.humedad <= 6:
            CCRecepcionMateriaPrima.objects.filter(pk=instance.pk).update(estado_cc='1')
        else:
            CCRecepcionMateriaPrima.objects.filter(pk=instance.pk).update(estado_cc='0')
            RecepcionMp.objects.filter(pk=instance.recepcionmp.pk).update(estado_recepcion='4')
            GuiaRecepcionMP.objects.filter(pk=instance.recepcionmp.guiarecepcion.pk).update(estado_recepcion='4')
    #     