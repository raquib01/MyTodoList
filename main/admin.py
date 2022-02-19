from django.contrib import admin
from main.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete', 'modified_on']
    list_editable = ['complete']
