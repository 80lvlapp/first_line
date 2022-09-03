from django.contrib import admin
from .models import CoacheModel


@admin.register(CoacheModel)
class CoacheAdmin(admin.ModelAdmin):
    list_display = ["id", 'name']
