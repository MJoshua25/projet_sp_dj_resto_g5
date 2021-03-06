from django.db import models
from configuration.models import *

# Create your models here.
class Message(Timemodels):
    """Model definition for Message."""
    nom = models.CharField(max_length=250)
    sujet = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        """Meta definition for Message."""

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Newsletter(Timemodels):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email