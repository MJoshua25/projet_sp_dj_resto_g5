from django.db import models
from configuration.models import *

# Create your models here.
#----------------reservation-----------#
class Table (Timemodels):
     nom = models.CharField(max_length=255)
     person = models.PositiveIntegerField()
     disponible = models.BooleanField(default=True)
      




class reservation(Timemodels):
    phone = models.IntegerField()
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message =  models.TextField()
    table = models.ForeignKey(Table,on_delete=models.CASCADE, related_name="tables")