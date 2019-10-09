from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TableAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'nom',
        'person',
        'disponible',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'phone',
        'nom',
        'email',
        'date',
        'time',
        'table',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'date',
        'table',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Table, TableAdmin)
_register(models.Reservation, ReservationAdmin)
