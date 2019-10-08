from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PresentationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'description',
        'logo',
        'license_site',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'description',
        'logo',
        'license_site',
    )
    raw_id_fields = ('working_hour',)


class PosteAdmin(admin.ModelAdmin):

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


class PersonnelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'prenom',
        'photo',
        'poste',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'poste',
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'prenom',
        'photo',
        'poste',
    )
    raw_id_fields = ('social',)


class SocialAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'personnel',
        'lien',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'personnel',
        'id',
        'statut',
        'date_add',
        'date_update',
        'personnel',
        'lien',
    )
    raw_id_fields = ('icon',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Presentation, PresentationAdmin)
_register(models.Poste, PosteAdmin)
_register(models.Personnel, PersonnelAdmin)
_register(models.Social, SocialAdmin)
