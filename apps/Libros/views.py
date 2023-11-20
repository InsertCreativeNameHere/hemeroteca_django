from django.shortcuts import render
from django.http import HttpResponse
from .models import libro,copy,publication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import libroSerializer,copySerializer,publicacionSerializer,copyBasicSerializer

from rest_framework.permissions import IsAuthenticated, BasePermission

class lectorPermision(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list": return  request.user.rol == 3

class TokenPermision(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class InventarioPermision(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create": return  request.user.rol == 2
        if view.action == "update": return  request.user.rol == 2
        if view.action == "list": return  request.user.rol == 2
        if view.action == "partial_update": return  request.user.rol == 2

class AdminPermision(BasePermission):
    def has_permission(self, request, view):
        return  request.user.rol == 4


# Create your views here.


class libroViewSet(viewsets.ModelViewSet):
    
    permission_classes = [ TokenPermision,InventarioPermision | AdminPermision | lectorPermision]
    serializer_class = libroSerializer
    queryset = libro.objects.all()
    

class copyViewSet(viewsets.ModelViewSet):
    permission_classes = [ TokenPermision,InventarioPermision | AdminPermision]
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
    permission_classes = [ TokenPermision,InventarioPermision | AdminPermision]
    serializer_class = publicacionSerializer
    queryset = publication.objects.all()