from django.db import models
from apps.Users.models import user
from apps.Libros.models import copy

# Create your models here.
class loan(models.Model):
    date_loan = models.DateTimeField()
    date_end = models.DateTimeField()
    date_returned = models.DateTimeField(null=True)
    user = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    copy = models.ForeignKey(copy,on_delete=models.DO_NOTHING)

class Debt(models.Model):
    price = models.IntegerField()
    created_date = models.DateTimeField()
    loan = models.ForeignKey(loan,on_delete=models.DO_NOTHING)