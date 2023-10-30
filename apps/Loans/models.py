from django.db import models
from apps.Users.models import user
from apps.Libros.models import copy

# Create your models here.
class loan(models.Model):
    date_loan = models.DateTimeField()
    date_end = models.DateTimeField()
    user = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(copy,on_delete=models.DO_NOTHING)