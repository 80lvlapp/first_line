from django.db import models
from api.type_of_tournament.models import TypeOfTournamentModel


class TournamentModel(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Наименование")
    date_tournament = models.DateField(verbose_name="Дата турнира")
    venue = models.CharField(max_length=100, verbose_name="Место проведения")
    type_of_tornament = models.ForeignKey(TypeOfTournamentModel, on_delete=models.RESTRICT, verbose_name="Тип турнира")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name} {self.type_of_tornament} {self.date_tournament} {self.venue}"

    class Meta:
        db_table = "fl_tournament"
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
