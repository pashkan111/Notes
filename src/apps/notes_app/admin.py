from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'guid',
        'is_liked',
    )
    search_fields = ('id', 'name', 'guid')

