from rest_framework import serializers
from .models import area

class areaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = area
        fields = '__all__'