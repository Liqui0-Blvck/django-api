from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from recepcionmp.models import RecepcionMp, EnvasesGuiaRecepcionMp
from django.db.models import Count, Sum, Avg, FloatField, F
from django.contrib.contenttypes.models import ContentType
import math

@receiver(post_save, sender=PatioTechadoExterior)
def vincular_envases_a_guiapatio_despues_de_asignar_ubicacion_descarga(sender, instance, created, **kwargs):
    peso_total_recepcion = None
    print(peso_total_recepcion)
    if created and instance:
        pass
    else:
        if instance.ubicacion != '0':
            if instance.tipo_recepcion.model == 'recepcionmp':
                pkrecepcionmp = instance.lote_recepcionado.pk
                recepcion = RecepcionMp.objects.get(pk=pkrecepcionmp)
                peso_envase = recepcion.envases.first().peso
                print(peso_envase)
                peso_total_recepcion = (recepcion.kilos_brutos_1 + recepcion.kilos_brutos_2) - (peso_envase)
                print(peso_total_recepcion)
                n_envases_en_rel = recepcion.envasesguiarecepcionmp_set.all().count()
                if n_envases_en_rel == 1:
                    for x in recepcion.envasesguiarecepcionmp_set.all():
                        envase = x.envase.nombre
                        if envase == 'Granel':
                            print("GRANEL 1 rel en ENVASES")
                            cantidad_envases_granel = math.ceil(peso_total_recepcion / 400)
                            
                            peso_por_envase = peso_total_recepcion / cantidad_envases_granel
                            
                            for i in range(cantidad_envases_granel):
                                numero_bin_actual = i + 1
                                EnvasesPatioTechadoExt.objects.update_or_create(
                                    guia_patio=instance,
                                    variedad=x.variedad,
                                    numero_bin=numero_bin_actual,
                                    kilos_fruta = peso_por_envase
                                )
                            pass
                        else:
                            for xx in (n+1 for n in range(x.cantidad_envases)):
                                peso_por_envase = peso_total_recepcion / x.cantidad_envases
                                EnvasesPatioTechadoExt.objects.update_or_create(
                                    guia_patio=instance,
                                    variedad=x.variedad,
                                    numero_bin=xx,
                                    kilos_fruta = peso_por_envase
                                    )
                                
                            RecepcionMp.objects.filter(pk=pkrecepcionmp).update(estado_recepcion='5')
                else:
                    # listapksenvases = []
                    # for x in recepcion.envasesguiarecepcionmp_set.all():
                    #     listapksenvases.append(x.pk)
                    listapksenvases = recepcion.envasesguiarecepcionmp_set.values_list('pk', flat=True)
                    print(listapksenvases.count())
                    peso_total_recepcion = (recepcion.kilos_brutos_1 + recepcion.kilos_brutos_2) - (recepcion.kilos_tara_1 + recepcion.kilos_tara_2)
                    print("soy el peso fruto", peso_total_recepcion)
                    
                    for x in listapksenvases:
                        tiposenvases =  EnvasesGuiaRecepcionMp.objects.get(pk=x)
                        envase = tiposenvases.envase.nombre
                        if envase == 'Granel':
                            print("GRANEL +1 en rel en ENVASES")
                            pass
                        else:
                            for xx in (n+1 for n in range(tiposenvases.cantidad_envases)):
                                EnvasesPatioTechadoExt.objects.update_or_create(guia_patio=instance, variedad=tiposenvases.variedad, numero_bin=xx )
                            RecepcionMp.objects.all().filter(pk=pkrecepcionmp).update(estado_recepcion='5')
                            
            # elif instance.estado_cc == '0' and created:
            #     LoteRecepcionMpRechazadoPorCC.objects.update_or_create(recepcionmp=instance.recepcionmp, rechazado_por=instance.cc_registrado_por)
            #     RecepcionMp.objects.all().filter(pk=instance.recepcionmp.pk).update(estado_recepcion='4')
                
@receiver(post_save, sender=BodegaG1)
def vincular_bin_g1_a_binbodega(sender, instance, created, **kwargs):
    if created and instance:
        ct = ContentType.objects.get_for_model(BodegaG1)
        BinBodega.objects.update_or_create(tipo_binbodega=ct, id_binbodega=instance.pk)
                    
@receiver(post_save, sender=BodegaG1Reproceso)
def vincular_bin_g1_reproceso_a_binbodega(sender, instance, created, **kwargs):
    if created and instance:
        ct = ContentType.objects.get_for_model(BodegaG1Reproceso)
        BinBodega.objects.update_or_create(tipo_binbodega=ct, id_binbodega=instance.pk)                  

@receiver(post_save, sender=BodegaG2)
def vincular_bin_g2_a_binbodega(sender, instance, created, **kwargs):
    if created and instance:
        ct = ContentType.objects.get_for_model(BodegaG2)
        BinBodega.objects.update_or_create(tipo_binbodega=ct, id_binbodega=instance.pk)
                    
@receiver(post_save, sender=BodegaG2Reproceso)
def vincular_bin_g2_reproceso_a_binbodega(sender, instance, created, **kwargs):
    if created and instance:
        ct = ContentType.objects.get_for_model(BodegaG2Reproceso)
        BinBodega.objects.update_or_create(tipo_binbodega=ct, id_binbodega=instance.pk) 
        
@receiver(post_save, sender=BodegaResiduosReproceso)
def vincular_bin_rs_reproceso_a_binbodega(sender, instance, created, **kwargs):
    if created and instance:
        ct = ContentType.objects.get_for_model(BodegaResiduosReproceso)
        BinBodega.objects.update_or_create(tipo_binbodega=ct, id_binbodega=instance.pk) 
        
@receiver(post_save, sender=BodegaResiduos)
def vincular_bin_rs_a_binbodega(sender, instance, created, **kwargs):
    if created and instance:
        ct = ContentType.objects.get_for_model(BodegaResiduos)
        BinBodega.objects.update_or_create(tipo_binbodega=ct, id_binbodega=instance.pk) 