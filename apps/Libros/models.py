from django.db import models
from apps.Areas.models import area

# Create your models here.

class libro(models.Model):
    titulo = models.CharField(max_length=50,null=False,blank=False)
    tipo = models.CharField(max_length=50,null=False,blank=False)
    fecha_publicacion = models.DateField()
    editorial = models.CharField(max_length=49,null=False,blank=False)
    area = models.ForeignKey(area, on_delete=models.DO_NOTHING , null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.titulo