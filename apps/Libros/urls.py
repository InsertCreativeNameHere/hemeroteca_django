from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'libros', views.libroViewSet, basename='libros')
router.register(r'copias', views.copyViewSet, basename='copies')
router.register(r'publicaciones', views.publicationViewSet, basename='publications')

urlpatterns = [
]

urlpatterns = urlpatterns + router.urls