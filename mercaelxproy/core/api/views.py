# core/api/views.py
from rest_framework import viewsets, filters, mixins
from core.models import Provincia, Ciudad, Distrito
from .serializers import ProvinciaListSerializer, ProvinciaDetailSerializer, CiudadListSerializer, CiudadDetailSerializer, DistritoListSerializer, DistritoDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.api.pagination import StandardResultsSetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.signals import PROVINCIA_CAPITALES, CAPITALES
from common.mixins import ProtectedDeleteMixin

#----UD10.3.a-----
#Vistas de la API REST de la aplicación core
class ProvinciaListViewSet(mixins.ListModelMixin, 
                           viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para listar las provincias
    Hereda de ListModelMixin para listar las provincias y de GenericViewSet para tener acceso a las acciones CRUD
    Filtros de búsqueda, ordenación y paginación configurados con DjangoFilterBackend
    Ordenación por código y nombre
    Búsqueda por código y nombre
    Orden por defecto por código
    Sin paginación
    """
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend] #Filtros de Django
    ordering_fields = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre']
    ordering = ['codigo']
    pagination_class = None

class ProvinciaDetailViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             ProtectedDeleteMixin, #----UD10.3.b---- # Importar el mixin ProtectedDeleteMixin
                             viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para crear, ver, actualizar y eliminar una provincia
    Hereda de CreateModelMixin para crear una provincia, RetrieveModelMixin
    para ver una provincia, UpdateModelMixin para actualizar una provincia y
    ProtectedDeleteMixin para eliminar una provincia
    Metodo create sobrescrito para crear una ciudad con el nombre de la capital de la provincia si existe
    """
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaDetailSerializer

    #----UD10.3.c-----
    #Sobreescribir el método create para crear una ciudad con el nombre de la capital de la provincia
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = Provincia.objects.get(pk=response.data["id"])
        capital_name = PROVINCIA_CAPITALES.get(instance.nombre) #Obtener el nombre de la capital de la provincia
        if capital_name:
            city_code = next((k for k, v in CAPITALES.items() if v == capital_name), None) #Obtener el código de la capital de la provincia
            if city_code:
                Ciudad.objects.create(
                    nombre=capital_name,
                    codigo=city_code,
                    provincia=instance
                )
        return response

class CiudadListViewSet(mixins.ListModelMixin, 
                        viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para listar las ciudades
    Hereda de ListModelMixin para listar las ciudades y de GenericViewSet para tener acceso a las acciones CRUD
    Filtros de búsqueda, ordenación y paginación configurados con DjangoFilterBackend
    Ordenación por código y nombre
    Búsqueda por código, nombre, descripción, código de la provincia y nombre de la provincia
    Filtro por provincia
    Orden por defecto por código
    Paginación estándar
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre', 'descripcion', 'provincia__codigo', 'provincia__nombre']
    filterset_fields = ['provincia']
    ordering = ['codigo']
    pagination_class = StandardResultsSetPagination

class CiudadDetailViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          ProtectedDeleteMixin,
                          viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para crear, ver, actualizar y eliminar una ciudad
    Hereda de CreateModelMixin para crear una ciudad, RetrieveModelMixin
    para ver una ciudad, UpdateModelMixin para actualizar una ciudad y
    ProtectedDeleteMixin para eliminar una ciudad
    """
    
    queryset = Ciudad.objects.all()
    serializer_class = CiudadDetailSerializer

class DistritoListViewSet(mixins.ListModelMixin, 
                          viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para listar los distritos
    Hereda de ListModelMixin para listar los distritos y de GenericViewSet para tener acceso a las acciones CRUD
    Filtros de búsqueda, ordenación y paginación configurados con DjangoFilterBackend
    Ordenación por nombre
    Búsqueda por nombre, código de la ciudad, nombre de la ciudad, código de la provincia y nombre de la provincia
    Filtro por ciudad
    Orden por defecto por nombre
    Paginación estándar
    """
    queryset = Distrito.objects.all()
    serializer_class = DistritoListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['nombre']
    search_fields = ['nombre', 'ciudad__codigo', 'ciudad__nombre', 'ciudad__provincia__codigo', 'ciudad__provincia__nombre']
    filterset_fields = ['ciudad']
    ordering = ['nombre']
    pagination_class = StandardResultsSetPagination

class DistritoDetailViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            ProtectedDeleteMixin,
                            viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para crear, ver, actualizar y eliminar un distrito
    Hereda de CreateModelMixin para crear un distrito, RetrieveModelMixin
    para ver un distrito, UpdateModelMixin para actualizar un distrito y
    ProtectedDeleteMixin para eliminar un distrito
    """
    queryset = Distrito.objects.all()
    serializer_class = DistritoDetailSerializer


#----UD10.3.d-----
#Vista de la API REST para capitalizar los nombres de las ciudades y provincias
class CapitalizeNamesView(APIView):
    """
    #----UD10.4-----
    Vista de la API REST para capitalizar los nombres de las ciudades y provincias
    """
    def get(self, request, *args, **kwargs):
        for city in Ciudad.objects.all():
            city.nombre = city.nombre.capitalize()
            city.save()

        for province in Provincia.objects.all():
            province.nombre = province.nombre.capitalize()
            province.save()
            
        return Response({"detail": "Nombres de ciudades y provincias actualizados"}, status=status.HTTP_200_OK)