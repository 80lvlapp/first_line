from django.contrib import admin
from .models import CategoryModel

# Register your models here.@admin.register(CountryModel)


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
