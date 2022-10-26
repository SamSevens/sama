# Register your models here.

from django.contrib import admin
from . import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}


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
        'topics',
        'slug'
    )

    list_filter = (
        'status',
        'topics',
    )
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
admin.site.register(models.Post, PostAdmin)
