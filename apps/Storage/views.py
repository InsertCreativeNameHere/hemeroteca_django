from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import EstanteSerializer,SeccionSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import Estante,Seccion

class TokenPermision(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class recepcionPermision(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list": return  request.user.rol == 1

        
class InventarioPermision(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create": return  request.user.rol == 2
        if view.action == "list": return  request.user.rol == 2
        if view.action == "update": return  request.user.rol == 2
        if view.action == "partial_update": return  request.user.rol == 2
        


class AdminPermision(BasePermission):
    def has_permission(self, request, view):
        return  request.user.rol == 4



class EstanteViewSet(viewsets.ModelViewSet):
    permission_classes = [ TokenPermision,recepcionPermision | AdminPermision | recepcionPermision]
    serializer_class =EstanteSerializer
    queryset = Estante.objects.all()

class SeccionViewSet(viewsets.ModelViewSet):
    permission_classes = [ TokenPermision,recepcionPermision | AdminPermision | recepcionPermision]
    serializer_class = SeccionSerializer
    queryset = Seccion.objects.all()