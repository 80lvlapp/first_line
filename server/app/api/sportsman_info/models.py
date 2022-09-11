from django.db import models
from api.sport_school.models import SportSchoolModel
from api.sportsman.models import SportsmanModel
from api.coache.models import CoacheModel



class SportsmanInfoModel(models.Model):
    period = models.DateField()
    sport_school = models.ForeignKey(SportSchoolModel, on_delete=models.RESTRICT)
    sportsman = models.ForeignKey(SportsmanModel, on_delete=models.RESTRICT)
    coache = models.ForeignKey(CoacheModel, on_delete=models.RESTRICT)
    insuranse = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.period} {self.sport_school} {self.sportsman} {self.coache}"

    class Meta:
        db_table = "fl_sportsman_info"
        unique_together = ('period', 'sport_school', 'sportsman', "coache")
        verbose_name = 'Запись по спортсмену'
        verbose_name_plural = 'Информация о спортсменах'
