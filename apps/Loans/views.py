from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import loanSerializer,debtSerializer

from .models import loan,Debt

from rest_framework.permissions import IsAuthenticated, BasePermission

# Create your views here.

class TokenPermision(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class recepcionPermision(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create": return  request.user.rol == 1
        if view.action == "update": return  request.user.rol == 1
        if view.action == "partial_update": return  request.user.rol == 1
        if view.action == "list": return  request.user.rol == 1

class AdminPermision(BasePermission):
    def has_permission(self, request, view):
        return  request.user.rol == 4


class loanViewSet(viewsets.ModelViewSet):
    permission_classes = [ TokenPermision,recepcionPermision | AdminPermision]
    serializer_class =loanSerializer
    queryset = loan.objects.all()

class debtViewSet(viewsets.ModelViewSet):
    permission_classes = [ TokenPermision,recepcionPermision | AdminPermision]
    serializer_class =debtSerializer
    queryset = Debt.objects.all()
