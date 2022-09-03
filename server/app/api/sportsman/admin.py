from django.contrib import admin
from .models import SportsmanModel


@admin.register(SportsmanModel)
class SportsmanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'date_birth']
