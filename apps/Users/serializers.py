from rest_framework import serializers
from .models import author,user,susbcription

class userSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user
        fields = '__all__'

class authorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = author
        fields = '__all__'

class subscriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = susbcription
        fields = '__all__'