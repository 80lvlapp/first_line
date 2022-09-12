from django.db import models

class TypeOfTournamentModel(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "fl_type_tournament"
        verbose_name = 'Категория'
        verbose_name_plural = 'Типы турниров'
