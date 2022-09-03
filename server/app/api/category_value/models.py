from unicodedata import category
from django.db import models
from api.category.models import CategoryModel


class CategoryValueModel(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "fl_category_value"
