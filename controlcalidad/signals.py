from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from recepcionmp.models import RecepcionMp, GuiaRecepcionMP, LoteRecepcionMpRechazadoPorCC
from bodegas.models import PatioTechadoExterior, CCGuiaInterna
from django.contrib.contenttypes.models import ContentType


@receiver(post_save, sender=CCRecepcionMateriaPrima)
def comprueba_si_aprueba_cc_por_humedad_recepcionmp(sender, instance, created, **kwargs):
    if instance and created:
        pass
    else:
        if instance.humedad <= 6:
            CCRecepcionMateriaPrima.objects.filter(pk=instance.pk).update(estado_cc='1')
            recepcionmp = RecepcionMp.objects.get(pk=instance.recepcionmp.pk)
            ctccrecepcionmp = ContentType.objects.get_for_model(CCRecepcionMateriaPrima)
            ctrecepcionmp = ContentType.objects.get_for_model(RecepcionMp)
            guiaccpatio = CCGuiaInterna.objects.update_or_create(tipo_cc_guia=ctccrecepcionmp, id_guia=instance.pk)
            guiacdcpation  = CCGuiaInterna.objects.get(pk=guiaccpatio[0].pk)
            guiapatioexterior = PatioTechadoExterior.objects.update_or_create(cc_guia=guiacdcpation, tipo_recepcion=ctrecepcionmp, id_recepcion=recepcionmp.pk, )
            print(f'Guia de Ingreso a Patio Techado Registrada con el N° {guiapatioexterior[0].pk}')
            if not recepcionmp.guiarecepcion.mezcla_variedades:
                GuiaRecepcionMP.objects.filter(pk=instance.recepcionmp.guiarecepcion.pk).update(estado_recepcion='4')
            else:
                GuiaRecepcionMP.objects.filter(pk=instance.recepcionmp.guiarecepcion.pk).update(estado_recepcion='2')
            
        else:
            CCRecepcionMateriaPrima.objects.filter(pk=instance.pk).update(estado_cc='0')
            RecepcionMp.objects.filter(pk=instance.recepcionmp.pk).update(estado_recepcion='4')
            LoteRecepcionMpRechazadoPorCC.objects.create(recepcionmp=instance.recepcionmp, rechazado_por=instance.cc_registrado_por)
            GuiaRecepcionMP.objects.filter(pk=instance.recepcionmp.guiarecepcion.pk).update(estado_recepcion='4')
    #     
