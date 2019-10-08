from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class InfoUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'ip',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'reseau',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'ip',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'reseau',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.InfoUser, InfoUserAdmin)
