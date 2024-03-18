from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin


class EnvasesGuiaPatioTechadoInlineAdmin(admin.TabularInline):
    model = EnvasesPatioTechadoExt
    extra = 1
    fields = ['id', 'estado_envase','variedad', 'numero_bin', 'kilos_fruta']



# Register your models here.
@admin.register(PatioTechadoExterior)
class PatioTechadoExtAdmin(admin.ModelAdmin):
    list_display = ('id', 'ubicacion','tipo_recepcion', 'cc_guia')
    search_fields = ['object_id',]
    inlines = [EnvasesGuiaPatioTechadoInlineAdmin,]