from django.apps import AppConfig


class SportsmanInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.sportsman_info'
    verbose_name = 'Информация о спортсменах'
