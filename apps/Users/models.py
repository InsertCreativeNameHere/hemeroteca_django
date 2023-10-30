from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(AbstractUser):
    REQUIRED_FIELDS = ["email"]
    

class susbcription(models.Model):
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class author(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
