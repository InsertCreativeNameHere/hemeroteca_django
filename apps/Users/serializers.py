from rest_framework import serializers
from .models import author,user,susbcription

class userSerializer(serializers.ModelSerializer):
    
    
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        _user = user.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
            email=validated_data['email'],
            rol=validated_data['rol']
        )
        return _user    
    
    class Meta:
        model = user
        fields = ("id","email","password","rol")

class authorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = author
        fields = '__all__'

class subscriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = susbcription
        fields = '__all__'