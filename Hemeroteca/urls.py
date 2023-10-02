from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include("apps.Libros.urls")),
    path('areas/', include("apps.Areas.urls"))
]
