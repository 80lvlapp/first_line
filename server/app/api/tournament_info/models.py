from django.db import models
from api.tournament.models import TournamentModel
from api.sportsman.models import SportsmanModel
from api.category_value.models import CategoryValueModel


class TournamentInfoModel(models.Model):
    period = models.DateField()
    tournament = models.ForeignKey(TournamentModel, on_delete=models.RESTRICT)
    sportsman = models.ForeignKey(SportsmanModel, on_delete=models.RESTRICT)
    category_value = models.ForeignKey(CategoryValueModel, on_delete=models.RESTRICT)
    points = models.IntegerField()
    place = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.period} {self.tournament} {self.sportsman} {self.category_value} {self.place}"

    class Meta:
        db_table = "fl_tournament_info"
        unique_together = ('period', 'tournament', 'sportsman', "category_value")
        verbose_name = 'Запись'
        verbose_name_plural = 'Информация о турнирах'
