from rest_framework import serializers
from .models import libro,copy,publication
from apps.Users.serializers import authorSerializer

class libroSerializer(serializers.ModelSerializer):
    
    cantidad_copias = serializers.SerializerMethodField()
    
    autor = authorSerializer()
    
    class Meta:
        model = libro
        fields = '__all__'
    
    def get_cantidad_copias(self,libro):
        cantidad = len(copy.objects.filter(libro_id = libro.id))
        return cantidad

class copySerializer(serializers.ModelSerializer):
    
    
    libro = libroSerializer()
    
    class Meta:
        model = copy
        fields = '__all__'

class copyBasicSerializer(serializers.ModelSerializer):
    

    
    class Meta:
        model = copy
        fields = '__all__'


class publicacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = publication
        fields = '__all__'