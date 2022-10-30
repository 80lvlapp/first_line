
from django.urls import path

from .views import TournamentViewSet


urlpatterns = [
    path("api/v1/tournaments",
         TournamentViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/tournaments/<int:pk>',
         TournamentViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
