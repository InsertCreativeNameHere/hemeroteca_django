from django.shortcuts import render
from .serializers import areaSerializer
from .models import area

from rest_framework import viewsets


# Create your views here.

class areaViewSet(viewsets.ModelViewSet):
    
    serializer_class = areaSerializer
    queryset = area.objects.all()