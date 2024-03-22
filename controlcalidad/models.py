from django.db import models
from recepcionmp.estados_modelo import *
from simple_history.models import HistoricalRecords as Historia
from controlcalidad.estados_modelo import *


def fotos_cc(instance, filename):
    return 'controlcalidad_recepcionmp/CDC_{0}/fotos_cc/{1}'.format(instance.pk, filename)

def fotos_cc_li(instance, filename):
    return 'controlcalidad_recepcionmp/Lote_{0}/fotos_cc/{1}'.format(instance.ccloteinterno.pk, filename)

def fotos_cc_tarja_seleccionada(instance, filename):
    return 'controlcalidad_seleccion/{0}/tarja/{1}'.format(instance.seleccion.pk, filename)




class CCRecepcionMateriaPrima(models.Model):
    recepcionmp = models.ForeignKey("recepcionmp.RecepcionMp", on_delete=models.CASCADE)
    cc_registrado_por = models.ForeignKey("auth.User", verbose_name="usuario_cc", on_delete=models.CASCADE, blank=True, null=True)
    #estado_cr = models.CharField(choices=ESTADOS_CONTROL_RENDIMIENTO, default='a', max_length=1)
    humedad = models.FloatField(blank=True, null=True)
    presencia_insectos = models.BooleanField(blank=True, null=True, default=False)
    observaciones = models.CharField(max_length=300, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado_cc = models.CharField(choices=ESTADO_CONTROL,max_length=1,default='2')
    control_rendimiento = models.ManyToManyField('self', through='CCRendimiento')
    historia = Historia()
    estado_aprobacion_cc = models.CharField(max_length=1, choices=ESTADO_APROBACION_CC_X_JEFATURA, default='0')
    fotos_cc = models.ManyToManyField('self', through='FotosCC')
    
    class Meta:
        verbose_name = ('CC Recepcion Mp')
        verbose_name_plural = ('1.0 - CC Recepcion Materia Prima')
        ordering = ('-pk', )

    def __str__(self):
        return "Control Calidad Lote N° %s"% (self.recepcionmp.pk)

class FotosCC(models.Model):
    ccrecepcionmp = models.ForeignKey("controlcalidad.CCRecepcionMateriaPrima", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=fotos_cc, blank=True, verbose_name='Fotos Control', null=True)




class CCRendimiento(models.Model):    
    cc_recepcionmp = models.ForeignKey("controlcalidad.CCRecepcionMateriaPrima", on_delete=models.CASCADE)
    #cc_guiarecepcionmp = models.ForeignKey("controlcalidad.CCGuiaRecepcionMateriaPrima", on_delete=models.SET_NULL, null=True)
    peso_muestra =  models.FloatField(blank=True, null =True, default=0.0)
    basura = models.FloatField(blank=True, null =True, default=0.0)
    pelon = models.FloatField(blank=True, null =True, default=0.0)
    cascara = models.FloatField(blank=True, null =True, default=0.0)
    pepa_huerto = models.FloatField(blank=True, null =True, default=0.0)
    pepa = models.FloatField(blank=True, null =True, default=0.0)
    ciega = models.FloatField(default=0.0)
    registrado_por = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    historia = Historia()
    aprobado_cc = models.BooleanField(default=False)
    es_contramuestra = models.BooleanField(default=False)
    esta_contramuestra = models.CharField(max_length=1, choices=ESTADO_CONTRAMUESTRA, default='0')
    

    class Meta:
        verbose_name = ('Muestra Lote RecepcionMP')
        verbose_name_plural = ('1.1 - Muestra Lote RecepcionMP')
        ordering = ('-pk', )

    def __str__(self):
        return "Muestra CC Lote N° %s"% (self.pk)



class CCPepa(models.Model):
    cc_rendimiento          = models.OneToOneField("controlcalidad.CCRendimiento", on_delete=models.CASCADE)    
    fecha_creacion          = models.DateTimeField(auto_now_add=True)
    fecha_modificacion      = models.DateTimeField(auto_now=True)    
    muestra_variedad        = models.FloatField(blank=True, null =True, default=0.0)
    daño_insecto            = models.FloatField(blank=True, null =True,default=0.0)
    hongo                   = models.FloatField(blank=True, null =True,default=0.0)
    doble                   = models.FloatField(blank=True, null =True,default=0.0)
    fuera_color             = models.FloatField(blank=True, null =True,default=0.0)
    vana_deshidratada       = models.FloatField(blank=True, null =True,default=0.0)
    punto_goma              = models.FloatField(blank=True, null =True,default=0.0)
    goma                    = models.FloatField(blank=True, null =True,default=0.0)       
    cc_pepaok               = models.BooleanField(default=False)
    cc_calibrespepaok       = models.BooleanField(default=False)
    pre_calibre             = models.FloatField(blank=True, null =True, default=0.0)
    calibre_18_20           = models.FloatField(blank=True, null =True, default=0.0)
    calibre_20_22           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_23_25           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_25_27           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_27_30           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_30_32           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_32_34           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_34_36           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_36_40           = models.FloatField(blank=True, null =True,default=0.0)
    calibre_40_mas          = models.FloatField(blank=True, null =True,default=0.0)
    observaciones           = models.CharField(max_length=300, blank=True, null=True)
    historia                = Historia()


    
    class Meta:
        verbose_name = ('CC Pepa muestra')
        verbose_name_plural = ('1.2 - CC Pepa muestras')
        ordering = ('-pk', )
    def __str__(self):
        return "CC de Pepa asociada a Muestra %s"% (self.cc_rendimiento.pk)   
    
