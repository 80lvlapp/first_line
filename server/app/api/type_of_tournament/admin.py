from django.contrib import admin
from .models import TypeOfTournamentModel

@admin.register(TypeOfTournamentModel)
class TypeOfTournamentAdmin(admin.ModelAdmin):
    list_display = ['name']
