from django.apps import AppConfig


class TournamentInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.tournament_info'
    verbose_name = 'Информация о турнирах'
