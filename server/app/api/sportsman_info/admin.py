from django.contrib import admin
from .models import SportsmanInfoModel


@admin.register(SportsmanInfoModel)
class ScoreScaleAdmin(admin.ModelAdmin):
    list_display = ['period', "sport_school", "sportsman", "coache"]
