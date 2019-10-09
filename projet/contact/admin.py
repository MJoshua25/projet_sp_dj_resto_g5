from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'nom',
        'sujet',
        'email',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'email')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Message, MessageAdmin)
_register(models.Newsletter, NewsletterAdmin)
