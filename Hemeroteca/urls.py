from django.contrib import admin
from django.urls import path,include

##Swagger

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Hemeroteca Django",
      default_version='v1',
      description="Implementacion de una hemeroteca utilizando el framework DJango",
      terms_of_service="https://github.com/InsertCreativeNameHere/hemeroteca_django",
      contact=openapi.Contact(email="javierandres.apontequevedo1@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    ##path('admin/', admin.site.urls),
    path('libros/', include("apps.Libros.urls")),
    path('users/', include("apps.Users.urls")),
    path('loans/', include("apps.Loans.urls")),
    path('almacenamiento/', include("apps.Storage.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
