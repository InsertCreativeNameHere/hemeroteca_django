from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    ##path('admin/', admin.site.urls),
    path('libros/', include("apps.Libros.urls")),
    path('users/', include("apps.Users.urls")),
    path('loans/', include("apps.Loans.urls"))
]
