from django.contrib import admin
from .models import SportsmanModel


@admin.register(SportsmanModel)
class CoacheAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'date_birth']
