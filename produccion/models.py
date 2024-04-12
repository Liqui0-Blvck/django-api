from django.db import models
from simple_history.models import HistoricalRecords as Historia
from .estados_modelo import *
from django.urls import reverse
from bodegas.estados_modelo import *
from django.contrib.contenttypes.fields import GenericForeignKey
from core.models import ModeloBaseHistorico, ModeloBase


class Produccion(ModeloBaseHistorico):
    estado                  = models.CharField(choices=ESTADOS_PRODUCCION, max_length=1, default='1')
    lotes                   = models.ManyToManyField("bodegas.EnvasesPatioTechadoExt", through= 'produccion.LotesPrograma') 
    tarjas_resultantes      = models.ManyToManyField("self", through= 'produccion.TarjaResultante') 
    registrado_por          = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    fecha_inicio_reproceso  = models.DateTimeField(blank=True, null = True)
    fecha_termino_reproceso = models.DateTimeField(blank=True, null = True)
    fecha_cierre_proceso    = models.DateTimeField(blank=True, null = True)
    fecha_termino_proceso   = models.DateTimeField(blank=True, null = True)
    fecha_pausa_proceso     = models.DateTimeField(blank=True, null = True)
    fecha_finpausa_proceso  = models.DateTimeField(blank=True, null = True)
    operarios               = models.ManyToManyField('core.Operario', through='produccion.OperariosEnProduccion')

    class Meta:
        verbose_name = "1.0 - Programa de Produccion"
        verbose_name_plural = "1.0 - Programas de Produccion"
        ordering = ['-pk',]

    def __str__(self):
        return 'Produccion N° %s'%(self.pk)
    
class OperariosEnProduccion(ModeloBase):
    produccion          = models.ForeignKey(Produccion, on_delete=models.CASCADE)
    operario            = models.ForeignKey('core.Operario', on_delete=models.CASCADE)
    kilos               = models.FloatField(default=0.0)
    dia                 = models.DateField()
    
    class Meta:
        verbose_name = '1.1 - Operario en Programa Produccion'
        verbose_name_plural = '1.1 -Operarios en Programas Produccion'
        constraints = [models.UniqueConstraint(
            name='%(app_label)s_%(class)s_unique_relationships',
            fields=['produccion', 'operario', 'dia']
        )]
        
    def __str__(self):
        return 'Operario %s %s en %s'%(self.operario.nombre, self.operario.apellido, self.produccion)

class LotesPrograma(ModeloBaseHistorico):
    produccion           = models.ForeignKey("produccion.Produccion", on_delete=models.CASCADE)
    bodega_techado_ext   = models.ForeignKey("bodegas.EnvasesPatioTechadoExt", on_delete=models.CASCADE)   
    bin_ingresado        = models.BooleanField(default=False)
    bin_procesado        = models.BooleanField(default=False)
    fecha_procesado      = models.DateTimeField(blank=True, null = True)
    procesado_por        = models.ForeignKey("auth.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "1.2 - Envase del Lote agregados a Produccion"
        verbose_name_plural = "1.2 - Envases del Lote en Producción"

    def __str__(self):
        return 'Envase N° %s en Programa N° %s'%(self.bodega_techado_ext,self.produccion.pk)

class TarjaResultante(ModeloBaseHistorico):
    tipo_resultante      = models.CharField(choices=TIPO_RESULTANTE, default='3', max_length=1)
    produccion           = models.ForeignKey("produccion.Produccion", on_delete=models.CASCADE)
    peso                 = models.FloatField()
    tipo_patineta        = models.FloatField(choices=TIPOS_BIN)
    registrado_por       = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank= True, null=True)
    cc_tarja             = models.BooleanField(default=False)
    fecha_cc_tarja       = models.DateTimeField(blank=True, null = True)
    ubicacion            = models.CharField(choices=UBICACION_TARJA, default='0', max_length=1)
    codigo_tarja         = models.CharField(max_length=9,blank=True, null=True, unique=True)
    calle_bodega         = models.CharField(max_length=2, choices=CALLE_BODEGA_2)

    class Meta:
        verbose_name = "1.3 - Tarja Resultante"
        verbose_name_plural = "1.3 - Tarjas Resultantes"

    def __str__(self):
        return '%s'%(self.codigo_tarja) 

class Reproceso(ModeloBaseHistorico):
    estado                  = models.CharField(max_length=1, choices=ESTADOS_REPROCESO, default="0")
    registrado_por          = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    fecha_inicio_reproceso  = models.DateTimeField(blank=True, null = True)
    fecha_termino_reproceso = models.DateTimeField(blank=True, null = True)
    fecha_cierre_proceso    = models.DateTimeField(blank=True, null = True)
    fecha_termino_proceso   = models.DateTimeField(blank=True, null = True)
    fecha_pausa_proceso     = models.DateTimeField(blank=True, null = True)
    fecha_finpausa_proceso  = models.DateTimeField(blank=True, null = True)
    bins                    = models.ManyToManyField("self", through= 'produccion.BinsEnReproceso') 
    tarjas_resultantes      = models.ManyToManyField("self", through= 'produccion.TarjaResultanteReproceso') 
    operarios               = models.ManyToManyField('core.Operario', through='produccion.OperariosEnReproceso')
    
    class Meta:
        verbose_name = '2.0 - Programa de Reproceso'
        verbose_name_plural = '2.0 - Programas de Reprocesos'
        ordering = ['pk']
        
    def __str__(self):
        return 'Reproceso N°%s'%(self.pk)
    
class OperariosEnReproceso(ModeloBase):
    reproceso           = models.ForeignKey(Reproceso, on_delete=models.CASCADE)
    operario            = models.ForeignKey('core.Operario', on_delete=models.CASCADE)
    kilos               = models.FloatField(default=0.0)

    
    class Meta:
        verbose_name = '2.1 - Operario en Reprocesp'
        verbose_name_plural = '2.1 - Operarios en Reprocesos'
        constraints = [models.UniqueConstraint(
            name='%(app_label)s_%(class)s_unique_relationships',
            fields=['reproceso', 'operario']
        )]
        
    def __str__(self):
        return 'Operario %s %s en %s'%(self.operario.nombre, self.operario.apellido, self.reproceso)
    
class BinsEnReproceso(ModeloBaseHistorico):
    reproceso           = models.ForeignKey(Reproceso, on_delete=models.CASCADE)
    limite_opciones     = models.Q(app_label = 'bodegas', model = 'bodegag1') | models.Q(app_label = 'bodegas', model = 'bodegag2') | models.Q(app_label = 'bodegas', model = 'bodegag1reproceso') | models.Q(app_label = 'bodegas', model = 'bodegag2reproceso')
    tipo_bin_bodega     = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to=limite_opciones)
    id_bin_bodega       = models.PositiveIntegerField()
    bin_bodega          = GenericForeignKey('tipo_bin_bodega', 'id_bin_bodega')
    bin_procesado       = models.BooleanField(default=False)
    fecha_procesado     = models.DateTimeField(blank=True, null=True)
    procesado_por       = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)

    
    class Meta:
        verbose_name = '2.2 - Bin Ingresado a Reproceso'
        verbose_name_plural = '2.2 - Bins Ingresados a Reprocesos'
        
    def __str__(self):
        return 'Bins %s en Reproceso N°%s'%(self.bin_bodega, self.reproceso.pk)
    
class TarjaResultanteReproceso(ModeloBaseHistorico):
    reproceso           = models.ForeignKey(Reproceso, on_delete=models.CASCADE)
    tipo_resultante     = models.CharField(max_length=1, choices=TIPO_RESULTANTE, default='3')
    peso                = models.FloatField(default=0.0)
    tipo_patineta       = models.FloatField(choices=TIPOS_BIN)
    cc_tarja            = models.BooleanField(default=False)
    codigo_tarja        = models.CharField(max_length=9,blank=True, null=True, unique=True)
    calle_bodega        = models.CharField(max_length=2, choices=CALLE_BODEGA_2)
    registrado_por      = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank= True, null=True)
 
    
    class Meta:
        verbose_name = '2.3 - Tarja Resultante Reproceso'
        verbose_name_plural = '2.3 - Tarjas Resultantes Reprocesos'
        
    def __str__(self):
        return '%s'%(self.codigo_tarja)