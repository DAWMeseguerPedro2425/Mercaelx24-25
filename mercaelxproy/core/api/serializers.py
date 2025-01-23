# mercaelxproy/core/serializers.py
from rest_framework import serializers
from core.models import Provincia, Ciudad, Distrito

#-----UD10.2-----
#Serializadores para las vistas de la API REST de la aplicación core
class ProvinciaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', '__str__']

class ProvinciaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class CiudadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['id', '__str__']

class CiudadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class DistritoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distrito
        fields = ['id', '__str__']


class DistritoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = '__all__'