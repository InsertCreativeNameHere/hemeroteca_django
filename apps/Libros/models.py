from django.db import models
from apps.Users.models import author
from apps.Storage.models import Seccion

# Create your models here.

class libro(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    edicion = models.IntegerField()
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(author,on_delete=models.DO_NOTHING)
##    editorial = models.CharField(max_length=49,null=False,blank=False)
##    area = models.ForeignKey(area, on_delete=models.DO_NOTHING , null=True, blank=True)
   
    
    def __str__(self) -> str:
        return self.nombre

class copy(models.Model):
    state = models.CharField(max_length=50)
    libro = models.ForeignKey(libro,on_delete=models.DO_NOTHING,null=False,blank=False)
    ubication = models.ForeignKey(Seccion,on_delete=models.DO_NOTHING)

class publication(models.Model):
    date = models.DateField()
    frecuency = models.IntegerField()