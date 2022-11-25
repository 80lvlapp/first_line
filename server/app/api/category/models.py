from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Наименование")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "fl_category"
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
