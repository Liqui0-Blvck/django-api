from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from import_export.admin import ImportExportModelAdmin

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Chofer)
admin.site.register(Camion)
admin.site.register(CargoPerfil)

class ImportacionDeGrupos(ImportExportModelAdmin):
    pass 
admin.site.register(Group, ImportacionDeGrupos)

@admin.register(User)
class ImportacionDeUsuarios(ImportExportModelAdmin):
    list_display = ('id','username', 'first_name', 'last_name', 'is_active', 'is_staff')




class PerfilesDeUsuarios(ImportExportModelAdmin):
    pass
admin.site.register(Perfil, PerfilesDeUsuarios)

@admin.register(PersonalizacionPerfil)
class PersonalizacionPerfilAdmin(admin.ModelAdmin):
    field = ['activa', 'estilo']


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
 
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]



# @admin.register(Perfil)
# class PerfilAdmin(admin.ModelAdmin):
#     list_display = ['user', 'sexo', 'direccion', 'comuna',
#     'telefono', 'celular', 'fnacimiento', 'valoracion', 'fotoperfil']


@admin.register(Operario)
class OperarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido', 'activo',  'lista_etiquetas')
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('etiquetas')

    def lista_etiquetas(self, obj):
        return u", ".join(o.name for o in obj.etiquetas.all())
    

@admin.register(Coloso)
class ColosoAdmin(admin.ModelAdmin):
    list_display = ('identificacion_coloso','tara', 'activo', 'fecha_creacion', )
@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    list_display = ('identificacion_tractor','tara', 'activo', 'fecha_creacion', )
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('etiquetas')

    def lista_etiquetas(self, obj):
        return u", ".join(o.name for o in obj.etiquetas.all())

@admin.register(TractorColoso)
class TractorColosoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'tractor', 'coloso_1', 'coloso_2', 'tara', 'fecha_creacion']
    
@admin.register(EtiquetasZpl)
class EtiquetasZplAdmin(ImportExportModelAdmin):
    list_display = ['pk', 'nombre']