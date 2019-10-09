from django.db import models
from configuration.models import *

# Create your models here.
class Menu(Timemodels):
    nom =  models.CharField(max_length=255)
    jour = DayOfTheWeekField(unique="True")
    plats = models.ManyToManyField('Plat',related_name='menu_plat')

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu du jour'

class Category(Timemodels):
    nom =  models.CharField(max_length=255)

    def __str__(self):
        
        return self.nom
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class Ingredient(Timemodels):
    nom =  models.CharField(max_length=255)

    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredient'


class Plat(Timemodels):
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="menu_plat")
    nom = models.CharField(max_length=160)
    description = models.TextField(null=True)
    prix = models.FloatField()
    ingredient = models.ManyToManyField(Ingredient,related_name="ingrediant_plat")
    image = models.ImageField(upload_to='restaurant/plat')
    speciale = models.BooleanField(default=False)
    def __str__(self):
        return self.nom

    class Meta:

        verbose_name = 'Plat'
        verbose_name_plural = 'Plats'