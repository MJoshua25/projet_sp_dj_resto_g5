from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class WorkingHourAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'jour',
        'start_hour',
        'end_hour',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'jour',
        'start_hour',
        'end_hour',
    )


class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'description',
        'image',
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
        'image',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_update', 'name')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'name',
    )
    search_fields = ('name',)


class ReserveConfigurationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'titre_formulaire',
        'sous_titre_formulaire',
        'image',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'titre_formulaire',
        'sous_titre_formulaire',
        'image',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.WorkingHour, WorkingHourAdmin)
_register(models.About, AboutAdmin)
_register(models.Social, SocialAdmin)
_register(models.ReserveConfiguration, ReserveConfigurationAdmin)
