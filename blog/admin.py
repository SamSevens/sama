# Register your models here.

from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    """displays title, datecreated and the date updated last"""
    list_display = (
        'title',
        'author',
        'created',
        'updated',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    list_filter = (
        'status',
        'topic'
    )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Post, PostAdmin)
