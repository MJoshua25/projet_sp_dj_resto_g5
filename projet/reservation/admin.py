from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TableAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'person',
        'disponible',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'disponible',
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'person',
        'disponible',
    )


class reservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'phone',
        'nom',
        'email',
        'date',
        'time',
        'message',
        'table',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'date',
        'table',
        'id',
        'statut',
        'date_add',
        'date_update',
        'phone',
        'nom',
        'email',
        'date',
        'time',
        'message',
        'table',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Table, TableAdmin)
_register(models.reservation, reservationAdmin)
