from recepcionmp.models import *
from django.db.models import Count, Sum, Avg, FloatField, F


def calcula_peso_envases(pklote):
    peso = EnvasesGuiaRecepcionMp.objects.filter(recepcionmp = pklote).aggregate(peso_envases=Sum(F('envase__peso')*F('cantidad_envases'), output_field=FloatField()))['peso_envases']    
    return peso


def total_envases_lote(pklote):
    lote = RecepcionMp.objects.get(pk=pklote)
    envases = lote.envasesguiarecepcionmp_set.filter(recepcionmp=pklote).aggregate(total_envases=Sum('cantidad_envases'))['total_envases']
    return envases