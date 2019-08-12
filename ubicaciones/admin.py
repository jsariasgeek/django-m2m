from django.contrib import admin
from .models import Region, Municipio

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class RegionInline(admin.TabularInline):
    model = Region.municipios.through
    extra = 0

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    inlines = [RegionInline]


