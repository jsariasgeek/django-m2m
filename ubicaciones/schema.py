from graphene import Mutation, String, List, Field, Int, Boolean
from graphene_django.types import DjangoObjectType, ObjectType
import graphene
from .models import Municipio, Region

class MunicipioType(DjangoObjectType):
    class Meta:
        model = Municipio

class RegionType(DjangoObjectType):
    class Meta:
        model = Region


class CreateMunicipio(Mutation):
    class Arguments:
        codigo = Int(required=True)
        nombre = String(required=True)
        estado = String(required=True)
    
    ok = Boolean()
    municipio = Field(MunicipioType)

    @staticmethod
    def mutate(self, info, codigo, nombre, estado):
        try:
            municipio_instance = Municipio.objects.get(codigo=codigo)
            return CreateMunicipio(municipio=municipio_instance, ok=False)
        except Municipio.DoesNotExist:
            municipio_instance = Municipio(
                codigo = codigo,
                nombre = nombre,
                estado = estado
            )
            municipio_instance.save()
        
        return CreateMunicipio(ok=True, municipio=municipio_instance)


class CreateRegion(Mutation):
    class Arguments:
        codigo = Int(required=True)
        nombre = String(required=True)
    
    ok = Boolean()
    region = Field(RegionType)

    @staticmethod
    def mutate(self, info, codigo, nombre):
        try:
            region_instance = Region.objects.get(codigo=codigo)
            return CreateRegion(region=region_instance, ok=False)
        except Region.DoesNotExist:
            region_instance = Region(
                codigo = codigo,
                nombre = nombre
            )
            region_instance.save()
        
        return CreateRegion(ok=True, region=region_instance)

class Mutation(ObjectType):
    create_region = CreateRegion.Field()    
    create_municipio = CreateMunicipio.Field()

class Query(ObjectType):
    region = Field(RegionType, codigo=Int())
    all_regions = List(RegionType)
    all_municipios = List(MunicipioType)
    
    def resolve_region(self, info, **kwargs):
        codigo = kwargs.get('codigo')
        return Region.objects.get(codigo=codigo)
    

    def resolve_all_regions(self, info, **kwargs):
        return Region.objects.all()

    def resolve_all_municipios(self, info, **kwargs):
        return Municipio.objects.filter(estado='ac')

