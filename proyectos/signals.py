from django.db.models.signals import *
from django.dispatch import *
from .models import *
from .options_models import *

@receiver(post_save, sender = 'proyectos.Proyecto')
def add_base_services(sender, instance, created, **kwargs):
  if created and instance:
    servicios_tipo = instance.tipo_proyecto.servicioproyectotipo_set.all()
    for servicio in servicios_tipo:
      ServicioEnProyecto.objects.create(
        proyecto = instance,
        tipo = ServicioProyectoTipo.objects.get(pk = servicio.pk),
        costo_servicio = servicio.costo
      )