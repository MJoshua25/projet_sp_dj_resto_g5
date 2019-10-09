from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TemoignageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'nom',
        'job',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Temoignage, TemoignageAdmin)
