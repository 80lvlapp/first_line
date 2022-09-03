from django.contrib import admin
from .models import TournamentInfoModel


@admin.register(TournamentInfoModel)
class TournamentInfoAdmin(admin.ModelAdmin):
    list_display = ['period', "tournament", "sportsman", "category_value"]
