from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from . import views

router = DefaultRouter()

router.register(r'users', views.userViewSet, basename='users')
router.register(r'authors', views.authorViewSet, basename='author')
router.register(r'subsciptions', views.subscriptionViewSet, basename='subscriptions')

urlpatterns = [
    path('sign-up/', views.CreateUserView.as_view(), name='create_user'),
]

urlpatterns = urlpatterns + router.urls