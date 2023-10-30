from django.shortcuts import render
from django.http import HttpResponse
from .models import libro,copy,publication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import libroSerializer,copySerializer,publicacionSerializer,copyBasicSerializer

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
    

class copyViewSet(viewsets.ModelViewSet):
    
    serializer_class = copySerializer
    queryset = copy.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            params = self.request.query_params
            
            if params.get("basic"):
                return copyBasicSerializer
            
        if self.action == "create":
            params = self.request.query_params
            
            if params.get("basic"):
                return copyBasicSerializer
            
        return super().get_serializer_class()

class publicationViewSet(viewsets.ModelViewSet):
    
    serializer_class = publicacionSerializer
    queryset = publication.objects.all()