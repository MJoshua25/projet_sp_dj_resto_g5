from django.db import models
from configuration.models import *

# Create your models here.

class Temoignage(Timemodels):
    nom = models.CharField(max_length=160)
    commentaire = models.TextField()
    job = models.CharField(max_length=255)
        
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'