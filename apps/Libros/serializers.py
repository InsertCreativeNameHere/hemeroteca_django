from rest_framework import serializers
from .models import libro

class libroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = libro
        fields = '__all__'