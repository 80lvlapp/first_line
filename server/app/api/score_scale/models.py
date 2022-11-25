from django.db import models
from api.sport_school.models import SportSchoolModel
from api.type_of_tournament.models import TypeOfTournamentModel


class ScoreScaleModel(models.Model):
    period = models.DateField(verbose_name="Период")
    sport_school = models.ForeignKey(SportSchoolModel, on_delete=models.RESTRICT, verbose_name="Спортивная школа")
    type_tournament = models.ForeignKey(TypeOfTournamentModel, on_delete=models.RESTRICT, verbose_name="Тип турнира")
    place_from = models.IntegerField(verbose_name="От")
    place_to = models.IntegerField(verbose_name="До")
    numbers_of_points = models.IntegerField(verbose_name="Очки")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.period} {self.sport_school} {self.type_tournament}"

    class Meta:
        db_table = "fl_score_scale"
        unique_together = ('period', 'sport_school', 'type_tournament')
        verbose_name = 'Запись'
        verbose_name_plural = 'Шкала'
