from django.urls import path

from .views import SportsmanPointsReportViewSet, TournamentsSportsmenReportViewSet


urlpatterns = [
   path("api/v1/reports/sportsman-report",
         SportsmanPointsReportViewSet.as_view({'get': "list"})),

    path("api/v1/reports/tournaments-sportsman-report",
         TournamentsSportsmenReportViewSet.as_view({'get': "list"})),
]