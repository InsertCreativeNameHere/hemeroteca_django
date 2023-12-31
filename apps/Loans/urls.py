from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'loans', views.loanViewSet, basename='loans'),
router.register(r'debts', views.debtViewSet, basename='debts')

urlpatterns = [
]

urlpatterns = urlpatterns + router.urls