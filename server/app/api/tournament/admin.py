from django.contrib import admin
from .models import TournamentModel


@admin.register(TournamentModel)
class SportsmanAdmin(admin.ModelAdmin):
    list_display = ['name', 'venue', "date_tournament"]
