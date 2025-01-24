from rest_framework import serializers
from directorio_comercios.models import Asociacion, Categoria, Subcategoria, Comercio

#-----UD10.2-----
#Serializadores para las vistas de la API REST de la aplicación directorio_comercios
class AsociacionListSerializer(serializers.ModelSerializer):
    asociacion = serializers.SerializerMethodField()

    class Meta:
        model = Asociacion
        fields = ['id', 'asociacion']

    def get_asociacion(self, obj):
        return f"{obj.nombre} - {obj.ciudad.nombre}"

class AsociacionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociacion
        fields = '__all__'

class CategoriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', '__str__']

class CategoriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = ['id', '__str__']

class SubcategoriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class ComercioListSerializer(serializers.ModelSerializer):
    nombre_provincia_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Comercio
        fields = ['id', 'nombre_provincia_nombre']

    def get_nombre_provincia_nombre(self, obj):
        return f"{obj.nombre} - {obj.ciudad.nombre}"

class ComercioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comercio
        fields = '__all__'