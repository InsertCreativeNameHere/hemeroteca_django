from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import authorSerializer,userSerializer,subscriptionSerializer

from .models import author,user,susbcription

from rest_framework.permissions import IsAuthenticated, BasePermission

# Create your views here.

class TokenPermision(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class lectorPermision(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list": return  request.user.rol == 3

class AdminPermision(BasePermission):
    def has_permission(self, request, view):
        return  request.user.rol == 4

class recepcionPermision(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create": return  request.user.rol == 1
        if view.action == "list": return  request.user.rol == 1
        if view.action == "update": return  request.user.rol == 1
        if view.action == "partial_update": return  request.user.rol == 1

class authorViewSet(viewsets.ModelViewSet):
    permission_classes = [ TokenPermision,  AdminPermision | recepcionPermision | lectorPermision]
    serializer_class = authorSerializer
    queryset = author.objects.all()
    

class userViewSet(viewsets.ModelViewSet):
    permission_classes = [ TokenPermision,  AdminPermision]
    serializer_class = userSerializer
    queryset = user.objects.all()

class CreateUserView(CreateAPIView):
    
    model = user
    permission_classes = [AllowAny]
    serializer_class = userSerializer
    queryset = user.objects.all()

class subscriptionViewSet(viewsets.ModelViewSet):

    permission_classes = [ TokenPermision,  AdminPermision | recepcionPermision]
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