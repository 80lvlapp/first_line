from django.db import models

class SportSchoolModel(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Наименование")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "fl_sport_school"
        verbose_name = 'Спортивную школу'
        verbose_name_plural = 'Спортивные школы'
