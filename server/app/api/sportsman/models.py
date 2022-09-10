from django.db import models


class SportsmanModel(models.Model):
    MALE = "MALE"
    FEMALE = "FEMALE"
    GENDERS = [
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
    ]

    name = models.CharField(max_length=50, db_index=True)
    gender = models.CharField(max_length=6, choices=GENDERS, default=MALE)
    date_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name} {self.gender} {self.date_birth}"

    class Meta:
        db_table = "fl_sportsman"
        verbose_name = 'Спортсмена'
        verbose_name_plural = 'Спортсмены'
