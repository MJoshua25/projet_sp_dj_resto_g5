from django.db import models
from configuration.models import *

# Create your models here.
# class Timemodels(models.Model):
    
    
    
#     statut = models.BooleanField(default=False)
#     date_add =  models.DateTimeField(auto_now_add=True)
#     date_update =  models.DateTimeField(auto_now=True)
      
#     class Meta:
        
#         abstract = True
class Presentation(Timemodels):
    
    """Model definition for Presentation."""
        
    nom = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logo', )
    working_hour = models.ManyToManyField(WorkingHour,related_name='working_config')
    license_site = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Presentation."""

        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        """Unicode representation of Presentation."""
        return self.nom

class Poste(Timemodels):
    
    nom = models.CharField(max_length=160)
        
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Poste'
        verbose_name_plural = 'Postes'

class Personnel(Timemodels):
    
    nom = models.CharField(max_length=160)
    prenom = models.CharField(max_length=160)
    photo = models.ImageField(upload_to='photo_presonnel')
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE,related_name="poste_presonnel")

        
    def __str__(self):
        return self.nom+ " " + self.prenom

    class Meta:
        verbose_name = 'Cuisinier'
        verbose_name_plural = 'Cuisiniers'
            
class Social(Timemodels):
        # TODO: Define fields here
    icon = models.ForeignKey('Social', on_delete=models.CASCADE,related_name="social_icon")
    personnel = models.ForeignKey('Personnel', on_delete=models.CASCADE,related_name="personnel_social")
    lien = models.URLField(max_length=200)
        
    def __str__(self):
        return '{}'.format(self.name)
    
