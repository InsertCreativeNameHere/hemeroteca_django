from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import loanSerializer

from .models import loan

# Create your views here.

class loanViewSet(viewsets.ModelViewSet):
    
    serializer_class =loanSerializer
    queryset = loan.objects.all()
    
