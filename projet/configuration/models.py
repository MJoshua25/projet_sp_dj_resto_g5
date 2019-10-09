from django.db import models
from django.utils.translation import ugettext as _
from django.db.models import SmallIntegerField
# Create your models here.

DAY_OF_THE_WEEK = {
        '1' : _(u'Monday'),
        '2' : _(u'Tuesday'),
        '3' : _(u'Wednesday'),
        '4' : _(u'Thursday'),
        '5' : _(u'Friday'),
        '6' : _(u'Saturday'),
        '7' : _(u'Sunday'),
        
    }

class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=30
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)
         
    class Meta:
        
        abstract = True
           
            


class Timemodels(models.Model):
    
    statut = models.BooleanField(default=False)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
      
    class Meta:
        abstract = True
           
class WorkingHour(Timemodels):
    
    # TODO: Define fields here
    jour = DayOfTheWeekField(unique="True")
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    class Meta:
        verbose_name = "WorkingHour"
        verbose_name_plural = "WorkingHours"

    def __str__(self):
        
        return '{}  {} - {}'.format(self.jour,self.start_hour,self.end_hour)
           
class About(Timemodels):
    
    """Model definition for About."""

    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image_about', )

    class Meta:
        
        
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        pass
            
class Social(Timemodels):
    
    
    
    # TODO: Define fields here
    choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
    name = models.CharField(max_length=100,choices=choice)

    @property
    def font(self):
        
            
        if self.name == 'FB':
            font = 'fab fa-facebook-f'
        elif self.name == 'TW':
            font ='fab fa-twitter'
        elif self.name == 'INS':
            font ='fab fa-instagram'
        elif self.name == 'GOO':
            font ='fab fa-google-plus-g'
        return font
    class Meta:
            
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self):
            
        return '{}'.format(self.name)
            
           
class ReserveConfiguration(Timemodels):
    
    
    """Model definition for ReserveConfiguration."""

    titre_formulaire = models.CharField(max_length=255)
    sous_titre_formulaire = models.CharField(max_length=255)
    image = models.ImageField(upload_to='resrvation_back')


        # TODO: Define fields here

    class Meta:
        """Meta definition for ReserveConfiguration."""

        verbose_name = 'ReserveConfiguration'
        verbose_name_plural = 'ReserveConfigurations'
            
class About(Timemodels):
    
    
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image_about',)

    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.nom