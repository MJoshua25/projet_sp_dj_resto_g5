from django.db import models
from configuration.models import *
# Create your models here.
class InfoUser(Timemodels):

    ip = models.GenericIPAddressField()
    pays = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    reseau = models.CharField(max_length=50)

    def __str__(self):
        return self.ip 