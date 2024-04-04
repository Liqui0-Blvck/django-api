from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin


class EnvasesGuiaPatioTechadoInlineAdmin(admin.TabularInline):
    model = EnvasesPatioTechadoExt
    extra = 1
    fields = ['id', 'estado_envase','variedad', 'numero_bin', 'kilos_fruta']


@admin.register(BinBodega)
class BinBodegaAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_binbodega', 'id_binbodega', 'binbodega')
    
# Register your models here.
@admin.register(PatioTechadoExterior)
class PatioTechadoExtAdmin(admin.ModelAdmin):
    list_display = ('id', 'ubicacion','tipo_recepcion', 'cc_guia')
    search_fields = ['object_id',]
    inlines = [EnvasesGuiaPatioTechadoInlineAdmin,]
    
@admin.register(BodegaG1)
class BodegaG1Admin(admin.ModelAdmin):
    list_display = ('id', 'produccion', 'kilos_fruta')

@admin.register(BodegaG2)
class BodegaG2Admin(admin.ModelAdmin):
    list_display = ('id', 'produccion', 'kilos_fruta')
    
@admin.register(BodegaG1Reproceso)
class BodegaG1ReprocesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'reproceso', 'kilos_fruta')

@admin.register(BodegaG2Reproceso)
class BodegaG2ReprocesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'reproceso', 'kilos_fruta')

@admin.register(BodegaResiduos)
class BodegaResiduosAdmin(admin.ModelAdmin):
    list_display = ('id', 'produccion', 'kilos_residuo')

@admin.register(BodegaResiduosReproceso)
class BodegaResiduosReprocesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'reproceso', 'kilos_residuo')

