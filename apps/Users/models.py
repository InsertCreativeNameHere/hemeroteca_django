from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(AbstractUser):
    
    ROLES_HEMEROTECA = (
        (1,'Recepcion'),
        (2,'Inventarios'),
        (3,'Lector'),
        (4,'Administrador')
    )
    
    REQUIRED_FIELDS = ["email"]
    rol = models.IntegerField(choices=ROLES_HEMEROTECA, default=4)
    

class susbcription(models.Model):
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class author(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
