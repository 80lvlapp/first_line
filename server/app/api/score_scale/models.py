from django.db import models
from api.sport_school.models import SportSchoolModel
from api.type_of_tournament.models import TypeOfTournamentModel


class ScoreScaleModel(models.Model):
    period = models.DateField()
    sport_school = models.ForeignKey(SportSchoolModel, on_delete=models.RESTRICT)
    type_tournament = models.ForeignKey(TypeOfTournamentModel, on_delete=models.RESTRICT)
    place_from = models.IntegerField()
    place_to = models.IntegerField()
    numbers_of_points = models.IntegerField()
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
