from django.contrib import admin
from .models import Nino,Area_Dental,Area_Medica,Area_Psicologica,Area_Social,Idioma,Enfermedad,Etnia,Motivo_Ingreso,Fuente_Estre,Nivel_Nutricion,Relacion_Familia
from django.utils.safestring import mark_safe

# Register your models here.



class NinoAdmin(admin.ModelAdmin):
    '''Admin View for Nino'''

    list_display = ('nombre_nino','apellido_nino','sexo','motivo_ingreso','fecha_nacimiento','cui','fecha_evaluacion',)
    list_filter = ('fecha_evaluacion','motivo_ingreso',)
    search_fields = ('nombre_nino',)


class Area_DentalAdmin(admin.ModelAdmin):
    '''Admin View for Area_Dental'''

    list_display = ('nino','proxima_cita','diagnostico',)
    list_filter = ('proxima_cita',)
    search_fields = ('diagnostico',)

class Area_MedicaAdmin(admin.ModelAdmin):
    '''Admin View for Area_Medica'''

    list_display = ('nino','peso','altura','nivel_nutricion',)
    

class Area_SocialAdmin(admin.ModelAdmin):
    '''Admin View for Area_Social'''

    list_display = ('nino','relacion_familiar','fuente_estres','visitas_autorizadas',)

class Area_PsicologicaAdmin(admin.ModelAdmin):
    '''Admin View for Area_Psicologica'''

    list_display = ('nino','estado_emocional','percepcion_calidad_vida','enfermedad',)
    
    
admin.site.register(Nino,NinoAdmin)
admin.site.register(Area_Dental,Area_DentalAdmin)
admin.site.register(Area_Medica,Area_MedicaAdmin)
admin.site.register(Area_Psicologica,Area_PsicologicaAdmin)
admin.site.register(Area_Social,Area_SocialAdmin)
admin.site.register(Enfermedad)
admin.site.register(Etnia)
admin.site.register(Motivo_Ingreso)
admin.site.register(Nivel_Nutricion)
admin.site.register(Fuente_Estre)
admin.site.register(Relacion_Familia)
admin.site.register(Idioma)
