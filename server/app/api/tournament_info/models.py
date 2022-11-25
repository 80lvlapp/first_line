from django.db import models
from api.tournament.models import TournamentModel
from api.sportsman.models import SportsmanModel
from api.category_value.models import CategoryValueModel


class TournamentInfoModel(models.Model):
    period = models.DateField(verbose_name="Период")
    tournament = models.ForeignKey(TournamentModel, on_delete=models.RESTRICT, verbose_name="Турнир")
    sportsman = models.ForeignKey(SportsmanModel, on_delete=models.RESTRICT, verbose_name="Спортсмен")
    category_value = models.ForeignKey(CategoryValueModel, on_delete=models.RESTRICT, verbose_name="Категория")
    points = models.IntegerField(verbose_name="Очки")
    place = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Место")
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
