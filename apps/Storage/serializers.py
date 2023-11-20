from rest_framework import serializers
from .models import Estante, Seccion

class EstanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estante
        fields = '__all__'
    

class SeccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seccion
        fields = '__all__'
    