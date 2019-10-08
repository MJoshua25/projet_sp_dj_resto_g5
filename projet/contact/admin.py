from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'sujet',
        'email',
        'message',
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
        'sujet',
        'email',
        'message',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_update', 'email')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'email',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Message, MessageAdmin)
_register(models.Newsletter, NewsletterAdmin)
