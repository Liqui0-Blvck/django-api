from django.db import models
from cuentas.models import *
from core.models import *
from .options_models import *
from django.contrib.contenttypes.models import *
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class BasesProyectoTipo(ModeloBase):
  nombre = models.CharField(max_length=255)
  bases = models.ManyToManyField('self', through = 'proyectos.ServicioProyectoTipo')
  
  
class ServicioProyectoPersonalizado(ModeloBase):
  nombre = models.CharField(max_length=255)
  descripcion = models.TextField(null=True, blank=True)
  costo = models.IntegerField(default=0)
  

class ServicioProyectoTipo(ModeloBase):
  nombre = models.CharField(max_length=255)
  descripcion = models.TextField(null=True, blank=True)
  costo = models.IntegerField(default=0)
  tipo_base = models.ForeignKey('proyectos.BasesProyectoTipo', on_delete = models.CASCADE, null=True)


class Proyecto(ModeloBase):
  nombre = models.CharField(max_length=255)
  cliente = models.ForeignKey('clientes.Cliente', on_delete = models.CASCADE)
  registrado_por = models.ForeignKey(User, on_delete = models.CASCADE)
  tipo_proyecto = models.ForeignKey('proyectos.BasesProyectoTipo', on_delete = models.CASCADE)
  servicios = models.ManyToManyField('self', through = 'proyectos.ServicioEnProyecto')    
  

class ServicioEnProyecto(ModeloBase):
  opciones = models.Q(app_label = 'proyectos', model = 'servicioproyectotipo') | models.Q(app_label = 'proyectos', model = 'servicioproyectopersonalizado')
  tipo_servicio = models.ForeignKey(ContentType, on_delete = models.CASCADE, limit_choices_to=opciones)
  id_servicio = models.PositiveIntegerField()
  servicio = GenericForeignKey('tipo_servicio', 'id_servicio')
  proyecto = models.ForeignKey('proyectos.Proyecto', on_delete = models.CASCADE)
  costo_servicio = models.IntegerField(default = 0)