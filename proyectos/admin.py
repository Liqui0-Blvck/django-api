from django.contrib import admin
from .models import *
# Register your models here.


class ServiciosEnProyectoINLINE(admin.TabularInline):
  model = ServicioEnProyecto
  

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
  list_display = ['id', 'nombre']
  inlines = [ServiciosEnProyectoINLINE, ]
    