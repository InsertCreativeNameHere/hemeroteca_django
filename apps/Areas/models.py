from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class area(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    descripcion = models.CharField(max_length=100,null=False,blank=False)
    
    def __str__(self) -> str:
        return self.nombre