from django.db import models

class Municipio(models.Model):

    estado_choices = (
        ('ac', 'activo'),
        ('in', 'inactivo')
    )

    codigo = models.PositiveSmallIntegerField(unique=True) #Codigo Unico
    nombre = models.CharField(max_length=60)
    estado = models.CharField(max_length=2, choices=estado_choices, default='AC')

    def __str__(self):
        return self.nombre
    
    #Si el municipio esta desactivado tenemos que quitarlo 
    #de todas las regiones donde pertenezca
    # Esto para el momento de actualizar un Municipio
    def save(self, *args, **kwargs):
        if self.pk is not None:
            if self.estado == 'in':
                # borramos todas las regiones a las que pertenezca
                self.region_set.clear()
        super(Municipio, self).save(*args, **kwargs)

class Region(models.Model):
    codigo = models.PositiveSmallIntegerField(unique=True)
    nombre = models.CharField(max_length=60)
    municipios = models.ManyToManyField(Municipio, blank=True) # Region puede tener ninguno o varios municipios

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Regiones'
