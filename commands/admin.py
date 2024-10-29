from django.contrib import admin
from .models import Command

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['cid', 'user', 'name', 'description', 'command', 'tag', 'level', 'created_at', 'updated_at']
