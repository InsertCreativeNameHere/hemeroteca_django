from django.shortcuts import render
from django.http import HttpResponse
from .models import libro

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import libroSerializer

# Create your views here.

def librosIndex(request):
    return HttpResponse("<h1> Hola desde la app de Libros <h1>")

class librosApiView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        _libros = libro.objects.all()
        data_response = [{"titulo" : libro.titulo,
                          "tipo" : libro.tipo,
                          "fecha de publicacion" : libro.fecha_publicacion,
                          "Editorial" : libro.editorial,
                          } for libro in _libros]
        return Response(data_response)
    
    
    def post(self,request,*args,**kwargs):
        
        data = request.data 
        
        _libro = libro(titulo = data.get("titulo"), tipo = data.get("tipo"), fecha_publicacion = data.get("fecha"), editorial= data.get("editorial"))
        _libro.save()
        
        return Response({'message' : "Libro creado"})
    

class libroViewSet(viewsets.ModelViewSet):
    
    serializer_class = libroSerializer
    queryset = libro.objects.all()