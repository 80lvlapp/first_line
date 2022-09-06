from django.contrib import admin
from .models import CategoryValueModel


@admin.register(CategoryValueModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', "category"]
