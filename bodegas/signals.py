from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from recepcionmp.models import RecepcionMp, EnvasesGuiaRecepcionMp
from django.db.models import Count, Sum, Avg, FloatField, F
from django.contrib.contenttypes.models import ContentType

def calcula_peso_envases(pklote):
    peso = EnvasesGuiaRecepcionMp.objects.filter(recepcionmp = pklote).aggregate(peso_envases=Sum(F('envase__peso')*F('cantidad_envases'), output_field=FloatField()))['peso_envases']    
    return peso


def total_envases_lote(pklote):
    lote = RecepcionMp.objects.get(pk=pklote)
    envases = lote.envasesguiarecepcionmp_set.filter(recepcionmp=pklote).aggregate(total_envases=Sum('cantidad_envases'))['total_envases']
    return envases

@receiver(post_save, sender=PatioTechadoExterior)
def vincular_envases_a_guiapatio_despues_de_asignar_ubicacion_descarga(sender, instance, created, **kwargs):
    if created and instance:
        pass
    else:
        if instance.ubicacion != '0':
            if instance.tipo_recepcion.model == 'recepcionmp':
                pkrecepcionmp = instance.lote_recepcionado.pk
                recepcion = RecepcionMp.objects.get(pk=pkrecepcionmp)
                n_envases_en_rel = recepcion.envasesguiarecepcionmp_set.all().count()
                if n_envases_en_rel == 1:
                    for x in recepcion.envasesguiarecepcionmp_set.all():
                        envase = x.envase.nombre
                        if envase == 'Granel':
                            print("GRANEL 1 rel en ENVASES")
                            pass
                        else:
                            for xx in (n+1 for n in range(x.cantidad_envases)):
                                EnvasesPatioTechadoExt.objects.update_or_create(guia_patio=instance, variedad=x.variedad, numero_bin=xx)
                                
                            RecepcionMp.objects.filter(pk=pkrecepcionmp).update(estado_recepcion='5')
                else:
                    # listapksenvases = []
                    # for x in recepcion.envasesguiarecepcionmp_set.all():
                    #     listapksenvases.append(x.pk)
                    listapksenvases = recepcion.envasesguiarecepcionmp_set.values_list('pk', flat=True)
                    print(listapksenvases.count())
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
                
      
                    
                    
        
        
        
# @receiver(post_save, sender=CCRecepcionMateriaPrima)
# def crear_guiapatio_en_bodega_lotes_aprobados(sender, instance, created, **kwargs):
#     if instance.estado_cc == '1' and created:
#         pkrecepcionmp = instance.recepcionmp.pk
#         ctcc = ContentType.objects.get(app_label='controlcalidad', model='ccrecepcionmateriaprima')
#         guiacc = CCGuiaInterna.objects.get(tipo_cc_guia=ctcc, id_guia=instance.pk)
#         ctrecepcion = ContentType.objects.get(app_label='recepcionmp', model='recepcionmp')
#         guiapatio = PatioTechadoExterior.objects.create(cc_guia=guiacc, content_type=ctrecepcion, object_id = pkrecepcionmp)
#         time.sleep(0.2)
#         cantidadenvases = instance.recepcionmp.envasesguiarecepcionmp_set.all().count()
#         if cantidadenvases == 1:
            # guiapatiot = PatioTechadoExterior.objects.get(pk=guiapatio.pk)
            # for x in instance.recepcionmp.envasesguiarecepcionmp_set.all():
            #     envase = x.envase.nombre
            #     if envase == 'Granel':
            #         pass
            #     else:
            #         for xx in (n+1 for n in range(x.cantidad_envases)):
            #             EnvasesPatioTechadoExt.objects.update_or_create(bodega_patio=guiapatiot, variedad=x.variedad, numero_bin=xx )
            #         RecepcionMp.objects.all().filter(pk=pkrecepcionmp).update(estado_recepcion='3')
#         else:
#             listapksenvases = []
#             for x in instance.recepcionmp.envasesguiarecepcionmp_set.all():
#                 listapksenvases.append(x.pk)
#             for i in range(len(listapksenvases)):
#                 tiposenvases =  EnvasesGuiaRecepcionMp.objects.get(pk=listapksenvases[i])
#                 print(tiposenvases)
#                 envase = tiposenvases.envase.nombre
#                 if envase == 'Granel':
#                     pass
#                 else:
#                     guiapatiot = PatioTechadoExterior.objects.get(pk=guiapatio.pk)
#                     cantidad_total_envases_lote = tiposenvases.cantidad_envases
#                     print(cantidad_total_envases_lote)
#                     for xx in (n+1 for n in range(cantidad_total_envases_lote)):
#                         EnvasesPatioTechadoExt.objects.create(bodega_patio=guiapatiot, variedad=tiposenvases.variedad, numero_bin=xx )
#                         print('aca')
#                     RecepcionMp.objects.all().filter(pk=pkrecepcionmp).update(estado_recepcion='3')
#     elif instance.estado_cc == '0' and created:
#         LoteRecepcionMpRechazadoPorCC.objects.update_or_create(recepcionmp=instance.recepcionmp, rechazado_por=instance.cc_registrado_por)
#         RecepcionMp.objects.all().filter(pk=instance.recepcionmp.pk).update(estado_recepcion='4')
        