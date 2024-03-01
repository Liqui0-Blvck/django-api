from django.db.models.signals import *
from django.dispatch import *
from .models import *
from .options_models import *
from django.db import transaction
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender = 'proyectos.Proyecto')
def add_base_services(sender, instance, created, **kwargs):
  if created and instance:
        with transaction.atomic():
            tipo_proyecto = instance.tipo_proyecto
            servicios_tipo = tipo_proyecto.servicioproyectotipo_set.all()
            
            print(servicios_tipo)
            for servicio_tipo in servicios_tipo:
              
              content_type = ContentType.objects.get(app_label='proyectos', model='servicioproyectotipo')
              
              print(content_type.id)
              servicio_en_proyecto = ServicioEnProyecto(
                  tipo_servicio_id=content_type.id,
                  id_servicio=servicio_tipo.id,
                  proyecto=instance,
                  costo_servicio=servicio_tipo.costo
              )
              servicio_en_proyecto.save()