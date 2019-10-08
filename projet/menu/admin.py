from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_update', 'nom', 'jour')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'jour',
    )
    raw_id_fields = ('plats',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_update', 'nom')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
    )


class IngredientAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_update', 'nom')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
    )


class PlatAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'categorie',
        'nom',
        'description',
        'prix',
        'image',
        'speciale',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'categorie',
        'speciale',
        'id',
        'statut',
        'date_add',
        'date_update',
        'categorie',
        'nom',
        'description',
        'prix',
        'image',
        'speciale',
    )
    raw_id_fields = ('ingredient',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Menu, MenuAdmin)
_register(models.Category, CategoryAdmin)
_register(models.Ingredient, IngredientAdmin)
_register(models.Plat, PlatAdmin)
