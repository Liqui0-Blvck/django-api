from django.db import models
from django.urls import reverse
from .estados_modelo import *
from django.contrib.contenttypes.fields import GenericForeignKey
from controlcalidad.estados_modelo import CALIDAD_FRUTA
from core.models import ModeloBase, ModeloBaseHistorico



class CCGuiaInterna(ModeloBase):
    opciones_cc = models.Q(app_label='controlcalidad', model='ccrecepcionmateriaprima') | models.Q(app_label='controlcalidad', model='cclotesinternos') 
    tipo_cc_guia = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to=opciones_cc)
    id_guia = models.PositiveIntegerField()
    cc_guia = GenericForeignKey('tipo_cc_guia', 'id_guia')
    
    class Meta:
        verbose_name = ('CC Guia Patio Exterior')
        verbose_name_plural = ('CC Guias de Patio Exterior')
    
    def __str__(self):
        
        return "%s"% (self.cc_guia)

class PatioTechadoExterior(ModeloBaseHistorico):
    cc_guia                 = models.ForeignKey("bodegas.CCGuiaInterna", on_delete=models.SET_NULL, null=True, blank=True)
    limite_opciones         = models.Q(app_label='recepcionmp', model='recepcionmp') | models.Q(app_label='recepcionmp', model='colososenlote')
    tipo_recepcion          = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to=limite_opciones)
    id_recepcion            = models.PositiveIntegerField()
    lote_recepcionado       = GenericForeignKey('tipo_recepcion', 'id_recepcion')
    ubicacion               = models.CharField(choices=UBICACION_PATIO_TECHADO_EXT, max_length=1, default='0')
    registrado_por          = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank= True, null=True)
    estado_lote             = models.CharField(choices=ESTADO_GUIA_PATIO_EXT, max_length=1, default='1')
    envases                 = models.ManyToManyField('self', through='bodegas.EnvasesPatioTechadoExt')
    procesado               = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = ('Bodega Patio Exterior')
        verbose_name_plural = ('Bodega Patio Exterior')
    
    def __str__(self):
        return "Bodega N°%s, %s"%(self.pk, self.lote_recepcionado)

class EnvasesPatioTechadoExt(ModeloBase):
    guia_patio           = models.ForeignKey('bodegas.PatioTechadoExterior', on_delete=models.CASCADE)
    kilos_fruta          = models.FloatField(default=0.0)
    fecha_creacion       = models.DateTimeField(auto_now_add=True)
    fecha_modificacion   = models.DateTimeField(auto_now=True)
    variedad             = models.CharField(max_length=30,choices=VARIEDAD)
    estado_envase        = models.CharField(choices=ESTADO_ENVASE_EN_PATIO_EXT, max_length=1, default='1')
    numero_bin           = models.PositiveIntegerField(default=0)
    
    
    class Meta:
        verbose_name = ('Envase Bodega Patio Exterior')
        verbose_name_plural = ('Envases Bodega Patio Exterior')
    
    def __str__(self):
        
        return "%s"% self.pk
        
class BinBodega(ModeloBaseHistorico):
    limite_opciones         = models.Q(app_label = 'bodegas', model = 'bodegag1') | models.Q(app_label = 'bodegas', model = 'bodegag1reproceso') | models.Q(app_label = 'bodegas', model = 'bodegag2') | models.Q(app_label = 'bodegas', model = 'bodegag2reproceso') 
    tipo_binbodega          = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to = limite_opciones)
    id_binbodega            = models.PositiveIntegerField()
    binbodega               = GenericForeignKey('tipo_binbodega', 'id_binbodega')
    procesado               = models.BooleanField(default=False)
    procesado_por           = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=True, null=True)
    estado_binbodega        = models.CharField(max_length=1, choices=ESTADO_BIN_BODEGA, default='1')
    
    def __str__(self):
        if self.tipo_binbodega == 'bodegag1' or  self.tipo_binbodega == 'bodegag2' or self.tipo_binbodega == 'bodegag1reproceso' or self.tipo_binbodega == 'bodegag2reproceso':
            return '%s'%self.binbodega.codigo_tarja
        else:
            return '%s'%self.pk

class BodegaResiduos(ModeloBaseHistorico):
    produccion              = models.OneToOneField("produccion.TarjaResultante",on_delete=models.CASCADE)
    kilos_residuo           = models.FloatField(default=0.0)
    fumigado                = models.BooleanField(default=False)  
    fecha_fumigacion        = models.DateTimeField(blank=True, null=True)    
    
    class Meta:
        verbose_name = 'Bodega Residuo'
        verbose_name_plural = 'Bodega Residuos'

    def __str__(self):
        return "%s"% (self.produccion.codigo_tarja)

class BodegaG1(ModeloBaseHistorico):
    produccion              = models.OneToOneField("produccion.TarjaResultante",on_delete=models.CASCADE)
    estado_bin              = models.CharField(choices=ESTADO_BIN_G1, max_length=1, default='1')
    kilos_fruta             = models.FloatField(default=0.0)
    variedad                = models.CharField(choices=VARIEDAD, max_length=3,default='---')
    calibre                 = models.CharField(choices=CALIBRES, max_length=2,default='0')
    calle_bodega            = models.CharField(max_length=2, choices=CALLE_BODEGA_1, default='-')
    estado_bin              = models.CharField(choices=ESTADO_BIN_G1, max_length=1, default='1')
    fumigado                = models.BooleanField(default=False)  
    fecha_fumigacion        = models.DateTimeField(blank=True, null=True)  


    class Meta:
        verbose_name = 'Bodega G1'
        verbose_name_plural = 'Bodega G1'


    
    def __str__(self):
        return "%s"% (self.produccion.codigo_tarja)
      
class BodegaG1Reproceso(ModeloBaseHistorico):
    reproceso               = models.OneToOneField("produccion.TarjaResultanteReproceso",on_delete=models.CASCADE)
    estado_bin              = models.CharField(choices=ESTADO_BIN_G1, max_length=1, default='1')
    kilos_fruta             = models.FloatField(default=0.0)
    variedad                = models.CharField(choices=VARIEDAD, max_length=3,default='---')
    calibre                 = models.CharField(choices=CALIBRES, max_length=2,default='0')
    calle_bodega            = models.CharField(max_length=2, choices=CALLE_BODEGA_1, default='-')
    estado_bin              = models.CharField(choices=ESTADO_BIN_G1, max_length=1, default='1')
    fumigado                = models.BooleanField(default=False)  
    fecha_fumigacion        = models.DateTimeField(blank=True, null=True)  


    class Meta:
        verbose_name = 'Bodega G1 Reproceso'
        verbose_name_plural = 'Bodegas G1 Reprocesos'
    
    def __str__(self):
        return "%s"% (self.reproceso.codigo_tarja)

class BodegaG2(ModeloBaseHistorico):
    produccion              = models.OneToOneField("produccion.TarjaResultante",on_delete=models.CASCADE, db_index=True, null=True, blank=True)
    estado_bin              = models.CharField(choices=ESTADO_BIN_G2, max_length=1, default='1')
    kilos_fruta             = models.FloatField(default=0.0)
    variedad                = models.CharField(choices=VARIEDAD, max_length=3,default='---')
    calibre                 = models.CharField(choices=CALIBRES, max_length=2,default='0')
    calle_bodega            = models.CharField(max_length=2, choices=CALLE_BODEGA_2, default='-')
    fumigado                = models.BooleanField(default=False)  
    fecha_fumigacion        = models.DateTimeField(blank=True, null=True)   

    class Meta:
        verbose_name = 'Bodega G2'
        verbose_name_plural = 'Bodega G2'

    def __str__(self):
        return "%s"% (self.produccion.codigo_tarja)

class BodegaG2Reproceso(ModeloBaseHistorico):
    reproceso               = models.OneToOneField("produccion.TarjaResultanteReproceso",on_delete=models.CASCADE)
    estado_bin              = models.CharField(choices=ESTADO_BIN_G2, max_length=1, default='1')
    kilos_fruta             = models.FloatField(default=0.0)
    variedad                = models.CharField(choices=VARIEDAD, max_length=3,default='---')
    calibre                 = models.CharField(choices=CALIBRES, max_length=2,default='0')
    calle_bodega            = models.CharField(max_length=2, choices=CALLE_BODEGA_2, default='-')
    fumigado                = models.BooleanField(default=False)  
    fecha_fumigacion        = models.DateTimeField(blank=True, null=True)   

    class Meta:
        verbose_name = 'Bodega G2 Reproceso'
        verbose_name_plural = 'Bodega G2 Reprocesos'

    def __str__(self):
        return "%s"% (self.reproceso.codigo_tarja)


# ######### Bodega G3 ##########
# class BodegaG3(models.Model):
#     seleccion          = models.ForeignKey("seleccion.TarjaSeleccionada", on_delete=models.CASCADE, null=True, blank=True)
#     fecha_creacion          = models.DateTimeField(auto_now_add=True)
#     fecha_modificacion      = models.DateTimeField(auto_now=True)
#     registrado_por          = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
#     historia                = Historia()
#     embalaje                = GenericRelation('embalaje.FrutaBodega')  
#     kilos_fruta             = models.FloatField(default=0.0)
#     estado_bin              = models.CharField(choices=ESTADO_BIN_G3_G4, max_length=1, default='1')
#     procesado_embalaje      = models.BooleanField(default=False)
#     variedad                = models.CharField(choices=VARIEDAD, max_length=3,default='---')
#     calibre                 = models.CharField(choices=CALIBRES, max_length=2,default='0')
#     calidad                 = models.CharField(max_length=1, choices=CALIDAD_FRUTA, default='0')
#     calle_bodega            = models.CharField(max_length=2, choices=CALLE_BODEGA_3, default='-')
#     dev_embalaje            = models.ForeignKey("embalaje.Embalaje", on_delete=models.SET_NULL, null=True, blank=True)
#     tarja_devuelta          = models.ForeignKey('bodegas.BodegaG3', on_delete=models.SET_NULL, null=True, blank=True)
#     fumigado                = models.BooleanField(default=False)  
#     fecha_fumigacion      = models.DateTimeField(blank=True, null=True)    
#     tarjas_agrupadas         = models.ForeignKey('bodegas.AgrupacionDeBinsBodegas', on_delete=models.SET_NULL, null=True, blank=True)
#     fruta_sobrante_agrupacion = models.ForeignKey('bodegas.FrutaSobranteDeAgrupacion', on_delete=models.SET_NULL, null=True, blank=True)
#     subproducto                 = models.ForeignKey('seleccion.BinSubProductoSeleccion', on_delete=models.CASCADE, null=True, blank=True)
        

#     class Meta:
#         verbose_name = 'Bodega G3'
#         verbose_name_plural = 'Bodega G3'

#     def __str__(self):
#         if self.seleccion != None:
#             return "%s"% (self.seleccion.codigo_tarja)
#         elif self.tarja_devuelta != None:
#             return "%s"%(self.tarja_devuelta.seleccion.codigo_tarja)
#         elif self.tarjas_agrupadas != None:
#             return "%s"%(self.tarjas_agrupadas.codigo_tarja)
#         elif self.subproducto != None:
#             return "%s"%(self.subproducto.codigo_tarja)

# import json

# ######### Bodega G4 ##########
# class BodegaG4(models.Model):
#     seleccion                   = models.ForeignKey("seleccion.TarjaSeleccionada", on_delete=models.SET_NULL, null=True, blank=True)
#     dev_embalaje                = models.ForeignKey("embalaje.Embalaje", on_delete=models.SET_NULL, null=True, blank=True)
#     fecha_creacion              = models.DateTimeField(auto_now_add=True)
#     fecha_modificacion          = models.DateTimeField(auto_now=True)
#     registrado_por              = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
#     kilos_fruta                 = models.FloatField(default=0.0)
#     historia                    = Historia()
#     estado_bin                  = models.CharField(choices=ESTADO_BIN_G3_G4, max_length=1, default='1')
#     embalaje                    = GenericRelation('embalaje.FrutaBodega')  
#     procesado_embalaje          = models.BooleanField(default=False)
#     calidad                     = models.CharField(max_length=1, choices=CALIDAD_FRUTA, default='0')
#     variedad                    = models.CharField(choices=VARIEDAD, max_length=3,default='---')
#     calibre                     = models.CharField(choices=CALIBRES, max_length=2,default='0')
#     fumigado                    = models.BooleanField(default=False)  
#     fecha_fumigacion            = models.DateTimeField(blank=True, null=True)   
#     calle_bodega                = models.CharField(max_length=2, choices=CALLE_BODEGA_4, default='-')
#     tarja_devuelta              = models.ForeignKey('bodegas.BodegaG4', on_delete=models.SET_NULL, null=True, blank=True)
#     tarjas_agrupadas            = models.ForeignKey('bodegas.AgrupacionDeBinsBodegas', on_delete=models.SET_NULL, null=True, blank=True)
#     fruta_sobrante_agrupacion   = models.ForeignKey('bodegas.FrutaSobranteDeAgrupacion', on_delete=models.SET_NULL, null=True, blank=True)
#     subproducto                 = models.ForeignKey('seleccion.BinSubProductoSeleccion', on_delete=models.CASCADE, null=True, blank=True)

#     class Meta:
#         verbose_name = 'Bodega G4'
#         verbose_name_plural = 'Bodega G4'
        
#     @property   
#     def get_codtarja(self):
#         if self.seleccion != None:
#             return "%s"% (self.seleccion.codigo_tarja)
#         elif self.tarja_devuelta != None:
#             return "%s"%(self.tarja_devuelta.seleccion.codigo_tarja)
        
    

#     def __str__(self):
#         if self.seleccion != None:
#             return "%s"% (self.seleccion.codigo_tarja)
#         elif self.tarja_devuelta != None:
#             return "%s"%(self.tarja_devuelta.seleccion.codigo_tarja)
#         elif self.tarjas_agrupadas != None:
#             return "%s"%(self.tarjas_agrupadas)
#         elif self.subproducto != None:
#             return "%s"%(self.subproducto.codigo_tarja)
#         else:
#             return 'none'
    

# class RegistrosTransferenciasG4G5(models.Model):
#     tarjas_bodegas = models.ManyToManyField('contenttypes.ContentType', through='TarjasTransferidas')
#     fecha_creacion          = models.DateTimeField(auto_now_add=True)
#     fecha_modificacion      = models.DateTimeField(auto_now=True)
#     registrado_por          = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
#     observaciones = models.CharField(max_length=160, blank=True, null=True)
#     estado_transferencia = models.CharField(max_length=1, default='0', choices=ESTADOS_TRANSFERENCIAS)
#     guia_completada = models.BooleanField(default=False)
#     guiaservicios           = models.ForeignKey("servicios_externos.GuiaServicioExterno", on_delete=models.CASCADE, blank=True, null=True)

    
#     class Meta:
#         verbose_name = 'Transferencia G4 a G5'
#         verbose_name_plural = 'Transferencias de Bins G4 a G5'
#         ordering = ('-fecha_creacion',)

#     def __str__(self):
#         return "Transferencia G4 a G5 id° %s"% (self.pk)
    
    
# class TarjasTransferidas(models.Model):
#     registro_transferencia  = models.ForeignKey("bodegas.RegistrosTransferenciasG4G5", on_delete=models.CASCADE)
#     limite_opciones         = models.Q(app_label = 'bodegas', model = 'bodegag1') | models.Q(app_label = 'bodegas', model = 'bodegag2') | models.Q(app_label = 'bodegas', model = 'bodegag3')  | models.Q(app_label = 'bodegas', model = 'bodegag4') | models.Q(app_label='bodegas_servicios', model='serviciobodegag3') | models.Q(app_label='bodegas_servicios', model='serviciobodegag4')
#     content_type            = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to = limite_opciones)
#     object_id               = models.PositiveIntegerField()
#     content_object          = GenericForeignKey('content_type', 'object_id')
#     estado_tarja            = models.CharField(max_length=1, choices=ESTADO_TARJA_TRANSFERIDA, default='0')
#     fecha_creacion          = models.DateTimeField(auto_now_add=True)
#     fecha_modificacion      = models.DateTimeField(auto_now=True)
#     registrado_por          = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
#     class Meta:
#         verbose_name = 'Tarja en Transferencia G4 a G5'
#         verbose_name_plural = 'Tarjas en Transferencias de Bins G4 a G5'

#     def __str__(self):
#         return "Tarja N°%s %s en Registro Transferencia Id: %s"% (self.pk, self.content_object, self.registro_transferencia.pk)
    
    
    

# ######### Bodega G5 ##########
# class BodegaG5(models.Model):
#     limite_opciones         = models.Q(app_label = 'bodegas', model = 'bodegag1') | models.Q(app_label = 'bodegas', model = 'bodegag2') | models.Q(app_label = 'bodegas', model = 'bodegag3')  | models.Q(app_label = 'bodegas', model = 'bodegag4') | models.Q(app_label = 'servicios_externos', model = 'guiaservicioexterno')  | models.Q(app_label='bodegas_servicios', model='serviciobodegag3') | models.Q(app_label='bodegas_servicios', model='serviciobodegag4')
#     content_type            = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to = limite_opciones)
#     object_id               = models.PositiveIntegerField()
#     content_object          = GenericForeignKey('content_type', 'object_id')
#     estado_bin              = models.CharField(max_length=50, choices=ESTADO_BIND_EN_FIGORIFICO, default='en_bodega')
#     created_date            = models.DateTimeField(auto_now_add=True)
#     modified_date           = models.DateTimeField(auto_now=True)
#     fecha_regkilos          = models.DateTimeField(blank=True,null=True)
#     embalaje                = GenericRelation('embalaje.FrutaBodega') 
#     calle_bodega            = models.CharField(max_length=2, choices=CALLE_BODEGA_G5, default='-')
#     historia                = Historia()
#     codigo_tarja            = models.CharField(max_length=9, blank=True, null=True)
#     kilos_fruta             = models.FloatField(default=0.0)
#     dev_embalaje            = models.ForeignKey("embalaje.Embalaje", on_delete=models.SET_NULL, null=True, blank=True)
#     tarja_devuelta          = models.ForeignKey('bodegas.BodegaG5', on_delete=models.SET_NULL, null=True, blank=True)
#     fumigado                = models.BooleanField(default=False)  
#     fecha_fumigacion      = models.DateTimeField(blank=True, null=True)   
#     tarjas_agrupadas         = models.ForeignKey('bodegas.AgrupacionDeBinsBodegas', on_delete=models.SET_NULL, null=True, blank=True)
#     fruta_sobrante_agrupacion = models.ForeignKey('bodegas.FrutaSobranteDeAgrupacion', on_delete=models.SET_NULL, null=True, blank=True)
    
#     class Meta:
#         verbose_name = "Bodega G5"
#         verbose_name_plural = "Bodega G5"
    
#     # @property
#     # def get_codtarja(self):
#     #     if self.content_type != None:
#     #         return '%s'%(self.content_object)
#     #     elif self.tarja_devuelta != None:
#     #         return "%s"%(self.tarja_devuelta.content_object)  

#     def __str__(self):
#         if self.content_type != None:
#             return '%s'%(self.content_object)
#         elif self.tarja_devuelta != None:
#             return "%s"%(self.tarja_devuelta.content_object)
#         elif self.tarjas_agrupadas != None:
#             return "%s"%(self.tarjas_agrupadas.codigo_tarja)



# ######### Bodega G6 ##########
# class BodegaG6(models.Model):
#     limite_opciones     = models.Q(app_label='plantaharina', model='binresultanteprogramaph') | models.Q(app_label='seleccion', model='tarjaseleccionada')
#     content_type        = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to=limite_opciones)
#     object_id           = models.PositiveIntegerField(blank=True, null=True)
#     content_object      = GenericForeignKey('content_type', 'object_id')
#     kilos_fruta         = models.FloatField(default=0.0)
#     created_date        = models.DateTimeField(auto_now_add=True)
#     modified_date       = models.DateTimeField(auto_now=True)
#     historia            = Historia()
#     estado_bin          = models.CharField(max_length=50, choices=ESTADO_BIND_EN_FIGORIFICO, default='en_bodega')
#     embalaje            = GenericRelation('embalaje.FrutaBodega')  
#     calle_bodega        = models.CharField(max_length=2, choices=CALLE_BODEGA_G5, default='-')
#     humedad             = models.FloatField(default=0.0)
#     piel_aderida        = models.FloatField(default=0.0)
#     calidad             = models.CharField(max_length=1, choices=CALIDAD_FRUTA, default='0')
#     dev_embalaje        = models.ForeignKey("embalaje.Embalaje", on_delete=models.SET_NULL, null=True, blank=True)
#     tarja_devuelta      = models.ForeignKey('bodegas.BodegaG6', on_delete=models.SET_NULL, null=True, blank=True)
#     fumigado            = models.BooleanField(default=False)  
#     fecha_fumigacion      = models.DateTimeField(blank=True, null=True)   
#     tarjas_agrupadas         = models.ForeignKey('bodegas.AgrupacionDeBinsBodegas', on_delete=models.SET_NULL, null=True, blank=True)
#     fruta_sobrante_agrupacion = models.ForeignKey('bodegas.FrutaSobranteDeAgrupacion', on_delete=models.SET_NULL, null=True, blank=True)  
    

#     class Meta:
#         verbose_name = 'Bodega G6'
#         verbose_name_plural = 'Bodega G6'
    
#     @property
#     def get_codtarja(self):
#         if self.content_type != None and self.object_id != None:
#             return '%s'%(self.content_object)
#         elif self.tarja_devuelta != None:
#             return "%s"%(self.tarja_devuelta.content_object)    

#     def __str__(self):
#         if self.content_object != None:
#             return '%s'%(self.content_object)
#         elif self.tarjas_agrupadas != None:
#             return "%s"%(self.tarjas_agrupadas.codigo_tarja)
#         elif self.tarja_devuelta != None:
#             return "%s"%(self.tarja_devuelta.content_object)
   
           
# from controlcalidad.estados_modelo import *

# ######### Bodega G7 ##########
# class BodegaG7(models.Model):
#     limite_opciones         = models.Q(app_label = 'plantaharina', model = 'binresultanteprocesoph')
#     content_type            = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to = limite_opciones)
#     object_id               = models.PositiveIntegerField(blank=True, null=True)
#     content_object          = GenericForeignKey()
#     estado_bin              = models.CharField(max_length=50, choices=ESTADO_BIND_EN_FIGORIFICO, default='en_bodega')
#     created_date            = models.DateTimeField(auto_now_add=True)
#     modified_date           = models.DateTimeField(auto_now=True)
#     historia                = Historia()
#     embalaje                = GenericRelation('embalaje.FrutaBodega')  
#     calle_bodega            = models.CharField(max_length=2, choices=CALLE_BODEGA_G5, default='-')
#     kilos_fruta             = models.FloatField(default=0.0)
#     dev_embalaje            = models.ForeignKey("embalaje.Embalaje", on_delete=models.SET_NULL, null=True, blank=True)
#     tarja_devuelta          = models.ForeignKey('bodegas.BodegaG3', on_delete=models.SET_NULL, null=True, blank=True)
#     humedad                 = models.FloatField(null=True, default=0.0)
#     piel_aderida            = models.FloatField(null=True, default=0.0)
#     granulometria           = models.FloatField(null=True, default=0.0)
#     parametro               = models.CharField(max_length=50, choices=PARAMETRO_HARINA, blank=True)
#     calidad                 = models.CharField(max_length=1, choices=CALIDAD_FRUTA, default='0')
#     fumigado                = models.BooleanField(default=False)  
#     fecha_fumigacion      = models.DateTimeField(blank=True, null=True)  
#     tarjas_agrupadas         = models.ForeignKey('bodegas.AgrupacionDeBinsBodegas', on_delete=models.SET_NULL, null=True, blank=True)
#     fruta_sobrante_agrupacion = models.ForeignKey('bodegas.FrutaSobranteDeAgrupacion', on_delete=models.SET_NULL, null=True, blank=True)
    

#     class Meta:
#         verbose_name = 'Bodega G7'
#         verbose_name_plural = 'Bodega G7'

#     def __str__(self):
#         if self.content_type != None and self.object_id != None:
#             return '%s'%(self.content_object)
#         elif self.tarja_devuelta != None:
#             return "%s"%(self.tarja_devuelta.content_object)
#         elif self.tarjas_agrupadas != None:
#             return "%s"%(self.tarjas_agrupadas.codigo_tarja)
        
# class FumigacionBodegas(models.Model):
#     codigo_fumigacion       = models.CharField(max_length=100, unique=True, null=True, blank=True)
#     fecha_creacion          = models.DateTimeField(auto_now_add=True)
#     fecha_modificacion      = models.DateTimeField(auto_now=True)
#     estado_fumigacion       = models.CharField(max_length=1, default='0', choices=ESTADOS_FUMIGACION)
#     bins_bodegas            = models.ManyToManyField('self', through='bodegas.BinsParaFumigacion')
#     registrado_por          = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
#     observaciones           = models.TextField(blank=True)
#     historia                = Historia()
#     fumigacion_armada       = models.BooleanField(default=False)
    
#     class Meta:
#         verbose_name = 'Fumigacion bodega'
#         verbose_name_plural = 'Fumigacion Bodegas'

#     def __str__(self):
#         return "Fumigacion N° %s"%(self.pk)
    

# class BinsParaFumigacion(models.Model):
#     fumigacion_bodega       = models.ForeignKey("bodegas.FumigacionBodegas", on_delete=models.CASCADE)
#     limite_opciones         = models.Q(app_label = 'bodegas', model = 'bodegag1') | models.Q(app_label = 'bodegas', model = 'bodegag2') | models.Q(app_label = 'bodegas', model = 'bodegag3')  | models.Q(app_label = 'bodegas', model = 'bodegag4') | models.Q(app_label = 'bodegas', model = 'bodegag5') | models.Q(app_label = 'bodegas', model = 'bodegag6') |models.Q(app_label = 'bodegas', model = 'bodegag7')
#     content_type            = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to = limite_opciones)
#     object_id               = models.PositiveIntegerField()
#     content_object          = GenericForeignKey('content_type', 'object_id')
    
#     class Meta:
#         verbose_name = 'Bin en Fumigacion'
#         verbose_name_plural = 'Bins en Fumigacion'

#     def __str__(self):
#         return "Fumigacion N° %s"%(self.pk)
    
# def random_id(lenght=6):
#         return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(lenght))    

# class AgrupacionDeBinsBodegas(models.Model):
#     fecha_creacion          = models.DateTimeField(auto_now_add=True)
#     fecha_modificacion      = models.DateTimeField(auto_now=True)
#     bins_agrupados          = models.ManyToManyField('self', through='bodegas.BinsParaAgrupacionDeBinsBodegas')
#     codigo_tarja            = models.CharField(max_length=9, blank=True, null=True)
#     registrado_por          = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
#     fruta_sobrante          = models.ForeignKey('bodegas.FrutaSobranteDeAgrupacion', on_delete=models.CASCADE, blank=True, null=True)
#     transferir_bodega       = models.CharField(max_length=2, choices=BODEGAS_PRODALMEN)
#     kilos_fruta             = models.FloatField(default=0.0, blank=True, null=True)
#     tipo_patineta           = models.FloatField(choices=TIPOS_BIN, blank=True, null=True)
#     tarja_agrupada          = models.BooleanField(default=False)
    
    
#     class Meta:
#         verbose_name = 'Agrupacion de Bin'
#         verbose_name_plural = 'Agrupacion de Bines'

#     def __str__(self):
#         return "%s"%(self.codigo_tarja)
    
    
    
    
#     def save(self, *args, **kwargs):
#         if not self.codigo_tarja:
#             self.codigo_tarja = self.transferir_bodega+'-{}'.format(random_id())
#         super(AgrupacionDeBinsBodegas, self).save(*args, **kwargs)

# class BinsParaAgrupacionDeBinsBodegas(models.Model):
#     agrupacion              = models.ForeignKey("bodegas.AgrupacionDeBinsBodegas", on_delete=models.CASCADE)
#     limite_opciones         = models.Q(app_label = 'bodegas', model = 'bodegag1') | models.Q(app_label = 'bodegas', model = 'bodegag2') | models.Q(app_label = 'bodegas', model = 'bodegag3')  | models.Q(app_label = 'bodegas', model = 'bodegag4') | models.Q(app_label = 'bodegas', model = 'bodegag5') | models.Q(app_label = 'bodegas', model = 'bodegag6') |models.Q(app_label = 'bodegas', model = 'bodegag7')
#     content_type            = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to = limite_opciones)
#     object_id               = models.PositiveIntegerField()
#     content_object          = GenericForeignKey('content_type', 'object_id')
#     class Meta:
#         verbose_name = 'Bins para Agrupacion de Bin'
#         verbose_name_plural = 'Bins Agrupacion de Bines'

#     def __str__(self):
#         return "%s"%(self.agrupacion)
    
# class FrutaSobranteDeAgrupacion(models.Model):
#     limite_opciones         = models.Q(app_label = 'bodegas', model = 'bodegag1') | models.Q(app_label = 'bodegas', model = 'bodegag2') | models.Q(app_label = 'bodegas', model = 'bodegag3')  | models.Q(app_label = 'bodegas', model = 'bodegag4') | models.Q(app_label = 'bodegas', model = 'bodegag5') | models.Q(app_label = 'bodegas', model = 'bodegag6') |models.Q(app_label = 'bodegas', model = 'bodegag7')
#     content_type            = models.ForeignKey('contenttypes.ContentType', on_delete=models.SET_NULL, null=True, limit_choices_to = limite_opciones)
#     object_id               = models.PositiveIntegerField()
#     content_object          = GenericForeignKey('content_type', 'object_id')
#     kilos_fruta             = models.FloatField(default=0.0)
    
#     class Meta:
#         verbose_name = 'Fruta Sobrante de Agrupación de Bin'
#         verbose_name_plural = 'Fruta Sobrante de Agrupación de Bin'

#     def __str__(self):
#         return "%s"%(self.content_object)
