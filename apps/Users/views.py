from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import authorSerializer,userSerializer,subscriptionSerializer

from .models import author,user,susbcription

# Create your views here.

class authorViewSet(viewsets.ModelViewSet):
    
    serializer_class = authorSerializer
    queryset = author.objects.all()
    

class userViewSet(viewsets.ModelViewSet):
    
    serializer_class = userSerializer
    queryset = user.objects.all()

class subscriptionViewSet(viewsets.ModelViewSet):

    serializer_class = subscriptionSerializer
    queryset = susbcription.objects.all()
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.data
        
        _suscriptions = susbcription.objects.filter(user_id = data.get("user"),start_date__lt = data.get("end_date"),end_date__gt = data.get("start_date"))
        if len(_suscriptions) > 0:
            return Response({"menssage":"Ya existe una suscripcion"},status=400)
        
        return super().create(request, *args, **kwargs)