from django.contrib import admin
from .models import SportSchoolModel

@admin.register(SportSchoolModel)
class CoacheAdmin(admin.ModelAdmin):
    list_display = ['name']
