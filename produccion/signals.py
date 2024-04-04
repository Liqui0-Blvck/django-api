from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from recepcionmp.models import RecepcionMp, EnvasesGuiaRecepcionMp
from django.db.models import Count, Sum, Avg, FloatField, F
from django.contrib.contenttypes.models import ContentType
from bodegas.models import *
import random, string
from controlcalidad.models import *


@receiver(post_save, sender=TarjaResultante)
def vincula_resultante_bodega_rs_g1_g2(sender, created, instance, **kwargs):
    def random_codigo_tarja(lenght=6):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(lenght))
    
    if created and instance:
        if instance.tipo_resultante == '3':
            BodegaG2.objects.update_or_create(produccion=instance, kilos_fruta=instance.peso)
            codigo = str('G2-')+random_codigo_tarja()
            instance.codigo_tarja = codigo
        elif instance.tipo_resultante == '2':
            BodegaResiduos.objects.update_or_create(produccion=instance, kilos_residuo=instance.peso)
            codigo = str('RS-')+random_codigo_tarja()
            instance.codigo_tarja = codigo
        elif instance.tipo_resultante == '1':
            BodegaG1.objects.update_or_create(produccion=instance, kilos_fruta=instance.peso)
            codigo = str('G1-')+random_codigo_tarja()
            instance.codigo_tarja = codigo
        instance.save()
        
@receiver(post_save, sender=TarjaResultanteReproceso)
def vincula_resultante_reproceso_bodega_rs_g1_g2(sender, created, instance, **kwargs):
    def random_codigo_tarja(lenght=6):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(lenght))
    if created and instance:
        if instance.tipo_resultante == '3':
            BodegaG2Reproceso.objects.update_or_create(reproceso=instance, kilos_fruta=instance.peso)
            codigo = str('G2-')+random_codigo_tarja()
            instance.codigo_tarja = codigo
        elif instance.tipo_resultante == '2':
            BodegaResiduosReproceso.objects.update_or_create(reproceso=instance, kilos_residuo=instance.peso)
            codigo = str('RS-')+random_codigo_tarja()
            instance.codigo_tarja = codigo
        elif instance.tipo_resultante == '1':
            BodegaG1Reproceso.objects.update_or_create(reproceso=instance, kilos_fruta=instance.peso)
            codigo = str('G1-')+random_codigo_tarja()
            instance.codigo_tarja = codigo
        instance.save()
        
@receiver(post_save, sender=TarjaResultante)
def crear_cc_tarja_resultante_y_vincular_a_tarja(sender, instance, created, **kwargs):   
    if instance.tipo_resultante == '3' or instance.tipo_resultante == '1':
        CCTarjaResultante.objects.update_or_create(tarja = instance)

@receiver(post_save, sender=TarjaResultanteReproceso)
def crear_cc_tarja_resultante_reproceso_y_vincular_a_cc(sender, instance, created, **kwargs):
    if instance.tipo_resultante == '3' or instance.tipo_resultante == '1':
        CCTarjaResultanteReproceso.objects.update_or_create(tarja = instance)