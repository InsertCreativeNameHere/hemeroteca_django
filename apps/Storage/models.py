from django.db import models
# Create your models here.
class Estante(models.Model):
    numero = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.numero
    

class Seccion(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    estante = models.ForeignKey(Estante, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre
    
    