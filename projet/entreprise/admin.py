from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PresentationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'nom',
        'description',
        'logo',
        'license_site',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )
    raw_id_fields = ('working_hour',)


class PosteAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'nom')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )


class PersonnelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'nom',
        'prenom',
        'photo',
        'poste',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )
    raw_id_fields = ('social',)


class SocialAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'personnel',
        'lien',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )
    raw_id_fields = ('icon',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Presentation, PresentationAdmin)
_register(models.Poste, PosteAdmin)
_register(models.Personnel, PersonnelAdmin)
_register(models.Social, SocialAdmin)
