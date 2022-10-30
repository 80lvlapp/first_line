
from django.urls import path

from .views import TournamentInfoViewSet


urlpatterns = [
    path("api/v1/tournaments-info",
         TournamentInfoViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/tournaments-info/<int:pk>',
         TournamentInfoViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
