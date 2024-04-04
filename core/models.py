
from django.db import models
from django.conf import settings
from .estados_modelo import *
from simple_history.models import HistoricalRecords as Historia
from django.core.validators import MinLengthValidator
from django.db.models import constraints
from phonenumber_field.modelfields import PhoneNumberField

class ModeloBase(models.Model):
    fecha_creacion          = models.DateTimeField(auto_now_add=True)
    fecha_modificacion      = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class ModeloBaseHistorico(models.Model):
    fecha_creacion          = models.DateTimeField(auto_now_add=True)
    fecha_modificacion      = models.DateTimeField(auto_now=True)
    historia                = Historia(inherit = True)
    
    
    class Meta:
        abstract = True




def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'perfiles/{0}/fotoperfil/{1}'.format(instance.user.username, filename)



###################perfil usuario##########################
class Perfil(ModeloBase):
    """Model definition for Socio."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='O')
    direccion = models.CharField(max_length=60, null=True, blank=True)
    comuna = models.CharField(max_length=30, null=True, blank=True)
    celular = models.CharField(max_length=20,null=True, blank=True)
    fnacimiento = models.DateField(blank=True, null=True, verbose_name='Fecha nacimiento')
    valoracion = models.IntegerField(default=0, blank=True)
    fotoperfil = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name='Foto Perfil', default='default.png')
    cargos = models.ManyToManyField('self', through='CargoPerfil')

    class Meta:
        verbose_name = ('Perfil Usuario')
        verbose_name_plural = ('Perfiles Usuarios')


    def __str__(self):
        return 'Perfil del usuario %s' % self.user
    

class CargoPerfil(ModeloBase):
    perfil = models.ForeignKey('core.perfil', on_delete=models.CASCADE)
    cargo = models.CharField(max_length=1, choices = CARGOS_PERFILES,  blank=True)
    


class CambioEstiloSitio(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    activa = models.BooleanField(default= False)
    estilo = models.CharField(max_length = 15, choices = ESTILO_CHOICES, default= 'minimal-theme')
    cabecera = models.CharField(max_length = 1, choices = CABECERA_CHOICES, default= '4')

    class Meta:
        verbose_name = ('Estilo sitio Usuario')
        verbose_name_plural = ('Estilo sitio Usuarios')



################### registros para recepcion de colosos #################


class Operario(ModeloBase):
    nombre          = models.CharField(max_length=50)
    apellido        = models.CharField(max_length=50)
    rut             = models.CharField(max_length=50, unique=True)
    tipo_operario   = models.CharField(max_length=10, choices=TIPOS_OPERARIO, default='seleccion' )
    activo          = models.BooleanField(default=True)
    etiquetas       = models.CharField(max_length=50, blank=True) # eliminar en proxima revision
    pago_x_kilo     = models.FloatField(default=50)

        

    class Meta:
        verbose_name = ("Operario")
        verbose_name_plural = ("Operarios Prodalmen")

    def __str__(self):
        return '%s %s'% (self.nombre, self.apellido)

class Coloso(ModeloBase):
    identificacion_coloso       = models.CharField(max_length=50, unique=True)
    tara                        = models.FloatField(default=0)
    activo                      = models.BooleanField(default=True) 
    etiquetas                   = models.CharField(max_length=50, blank=True)     

    

    class Meta:
        verbose_name = ("Coloso")
        verbose_name_plural = ("Colosos")

    def __str__(self):
        return '%s'% self.identificacion_coloso


class Tractor(ModeloBase):
    identificacion_tractor      = models.CharField(max_length=50, unique=True)
    tara                        = models.FloatField(default=0)
    activo                      = models.BooleanField(default=True)
    etiquetas                   = models.CharField(max_length=50, blank=True)    

    class Meta:
        verbose_name = ("Tractor")
        verbose_name_plural = ("Tractores")

    def __str__(self):
        return '%s'% self.identificacion_tractor
    
class TractorColoso(ModeloBase):
    tractor = models.ForeignKey(Tractor, on_delete=models.SET_NULL, null=True, blank=True)
    coloso_1 = models.ForeignKey(Coloso, related_name='primer_coloso', on_delete=models.SET_NULL, null=True, blank=True)
    coloso_2 = models.ForeignKey(Coloso, related_name='segundo_coloso', on_delete=models.SET_NULL, null=True, blank=True)
    tara = models.FloatField(default=0.0)
    
    class Meta:
        verbose_name = 'Tractor con Coloso'
        verbose_name_plural = 'Tractores con Colosos'
        
    def __str__(self):
        fecha = self.fecha_creacion
        fecha = fecha.strftime("%d-%m-%Y")
        if self.coloso_2 == None:
            return "Tractor %s con Coloso %s de %s Kgs, con Fecha del %s"%(self.tractor, self.coloso_1, self.tara, fecha)
        else:
            return "Tractor %s con Coloso %s y %s de %s Kgs, con Fecha del %s"%(self.tractor, self.coloso_1, self.coloso_2, self.tara, fecha)


class EtiquetasZpl(ModeloBase):
    nombre = models.CharField(max_length=70)
    zpl = models.TextField()
    
    class Meta:
        verbose_name = 'Etiqueta ZPL'
        verbose_name_plural = 'Etiquetas ZPL'

    def __str__(self):
        return "%s"%(self.nombre)
    

    
class Camion(ModeloBase):
    patente = models.CharField(max_length=6, validators=[MinLengthValidator(6)], unique=True)
    acoplado = models.BooleanField(default=False, blank = True, null=True)
    observaciones = models.TextField(max_length=150, blank = True, null=True)  
    class Meta:
        verbose_name = ('4.0 - Camion')
        verbose_name_plural = ('4.0 - Camiones')
  

    def __str__(self):
        patente2 = str(self.patente)
        if self.acoplado:
            acoplado_estado = "Con Acoplado"
        else:
            acoplado_estado = "Sin Acoplado"
        return "Patente %s, %s "% (patente2.upper(), acoplado_estado)




class Chofer(ModeloBase):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=11, unique=True)
    telefono = PhoneNumberField(blank=True)
    
    def nombre_completo(self):
        return "%s %s"% (self.nombre, self.apellido)
    

    class Meta:
        verbose_name = ('Chofer')
        verbose_name_plural = ('Choferes')

    def __str__(self):
        return '%s %s '%(self.nombre, self.apellido)