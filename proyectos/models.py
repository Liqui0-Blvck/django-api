from django.db import models
from cuentas.models import *
from core.models import *
from .options_models import *
# Create your models here.


class BasesProyectoTipo(ModeloBase):
  nombre = models.CharField(max_length=255)
  bases = models.ManyToManyField('self', through = 'proyectos.ServicioProyectoTipo')
  
  
class ServicioProyectoTipo(ModeloBase):
  nombre = models.CharField(max_length=255)
  descripcion = models.TextField(null=True, blank=True)
  costo = models.IntegerField(default=0)
  proyecto_tipo = models.ForeignKey('proyectos.BasesProyectoTipo', on_delete = models.CASCADE)


class Proyecto(ModeloBase):
  nombre = models.CharField(max_length=255)
  cliente = models.ForeignKey('clientes.Cliente', on_delete = models.CASCADE)
  registrado_por = models.ForeignKey(User, on_delete = models.CASCADE)
  tipo_proyecto = models.ForeignKey('proyectos.BasesProyectoTipo', on_delete = models.CASCADE)
  servicios = models.ManyToManyField('proyectos.ServicioProyectoTipo', through = 'proyectos.ServicioEnProyecto')    
  
  
class ServicioEnProyecto(ModeloBase):
  tipo = models.ForeignKey('proyectos.ServicioProyectoTipo', on_delete = models.CASCADE)
  proyecto = models.ForeignKey('proyectos.Proyecto', on_delete = models.CASCADE)
  costo_servicio = models.IntegerField(default=0)