# directorio_comercios/api/views.py
from rest_framework import viewsets, filters, mixins
from directorio_comercios.models import Asociacion, Categoria, Subcategoria, Comercio
from .serializers import AsociacionListSerializer, AsociacionDetailSerializer, CategoriaListSerializer, CategoriaDetailSerializer, SubcategoriaDetailSerializer, SubcategoriaListSerializer, ComercioListSerializer, ComercioDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.api.pagination import StandardResultsSetPagination
from common.mixins import ProtectedDeleteMixin


#----UD10.3.a-----
#Vistas de la API REST de la aplicación directorio_comercios
class AsociacionListViewSet(viewsets.ModelViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para listar las asociaciones
    Hereda de ModelViewSet para tener acceso a las acciones CRUD
    Filtros de búsqueda, ordenación y paginación configurados con DjangoFilterBackend
    Ordenación por nombre
    Búsqueda por nombre, dirección, correo electrónico y teléfono
    Filtro por ciudad
    Orden por defecto por nombre
    Paginación estándar
    """
    queryset = Asociacion.objects.all()
    serializer_class = AsociacionListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['nombre']
    search_fields = ['nombre', 'direccion', 'correo_electronico', 'telefono']
    filterset_fields = ['ciudad']
    ordering = ['nombre']
    pagination_class = StandardResultsSetPagination

class AsociacionDetailViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            ProtectedDeleteMixin,
                            viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para crear, ver, actualizar y eliminar una asociación
    Hereda de CreateModelMixin para crear una asociación, RetrieveModelMixin
    para ver una asociación, UpdateModelMixin para actualizar una asociación y
    ProtectedDeleteMixin para eliminar una asociación
    """
    queryset = Asociacion.objects.all()
    serializer_class = AsociacionDetailSerializer

class CategoriaListViewSet(viewsets.ModelViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para listar las categorías
    Hereda de ModelViewSet para tener acceso a las acciones CRUD
    Filtros de búsqueda, ordenación y paginación configurados con DjangoFilterBackend
    Ordenación por código y nombre
    Búsqueda por código y nombre
    Orden por defecto por código
    Paginación estándar
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre']
    ordering = ['codigo']
    pagination_class = StandardResultsSetPagination

class CategoriaDetailViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             ProtectedDeleteMixin,
                             viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para crear, ver, actualizar y eliminar una categoría
    Hereda de CreateModelMixin para crear una categoría, RetrieveModelMixin
    para ver una categoría, UpdateModelMixin para actualizar una categoría y
    ProtectedDeleteMixin para eliminar una categoría
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer

class SubcategoriaListViewSet(viewsets.ModelViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para listar las subcategorías
    Hereda de ModelViewSet para tener acceso a las acciones CRUD
    Filtros de búsqueda, ordenación y paginación configurados con DjangoFilterBackend
    Ordenación por código y nombre
    Búsqueda por código, nombre, código de la categoría y nombre de la categoría
    Filtro por categoría
    Orden por defecto por código
    Paginación estándar
    """
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre', 'categoria__codigo', 'categoria__nombre']
    filterset_fields = ['categoria']
    ordering = ['codigo']
    pagination_class = StandardResultsSetPagination

class SubcategoriaDetailViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                ProtectedDeleteMixin,
                                viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para crear, ver, actualizar y eliminar una subcategoría
    Hereda de CreateModelMixin para crear una subcategoría, RetrieveModelMixin
    para ver una subcategoría, UpdateModelMixin para actualizar una subcategoría y
    ProtectedDeleteMixin para eliminar una subcategoría
    """
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaDetailSerializer


class ComercioListViewSet(viewsets.ModelViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para listar los comercios
    Hereda de ModelViewSet para tener acceso a las acciones CRUD
    Filtros de búsqueda, ordenación y paginación configurados con DjangoFilterBackend
    Ordenación por nombre
    Búsqueda por nombre, dirección, correo electrónico y teléfono
    Filtro por ciudad y asociación
    Orden por defecto por nombre
    Paginación estándar
    """
    queryset = Comercio.objects.all()
    serializer_class = ComercioListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['nombre']
    search_fields = ['nombre', 'direccion', 'correo_electronico', 'telefono']
    filterset_fields = ['ciudad', 'asociacion']
    ordering = ['nombre']
    pagination_class = StandardResultsSetPagination

class ComercioDetailViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            ProtectedDeleteMixin,
                            viewsets.GenericViewSet):
    """
    #----UD10.4-----
    Vista de la API REST para crear, ver, actualizar y eliminar un comercio
    Hereda de CreateModelMixin para crear un comercio, RetrieveModelMixin
    para ver un comercio, UpdateModelMixin para actualizar un comercio y
    ProtectedDeleteMixin para eliminar un comercio
    """
    queryset = Comercio.objects.all()
    serializer_class = ComercioDetailSerializer