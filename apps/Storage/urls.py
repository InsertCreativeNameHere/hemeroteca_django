from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'secciones', views.EstanteViewSet, basename='secciones'),
router.register(r'estantes', views.SeccionViewSet, basename='estantes')

urlpatterns = [
]

urlpatterns = urlpatterns + router.urls