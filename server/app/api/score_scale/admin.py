from django.contrib import admin
from .models import ScoreScaleModel


@admin.register(ScoreScaleModel)
class ScoreScaleAdmin(admin.ModelAdmin):
    list_display = ['period', "sport_school", "type_tournament"]
