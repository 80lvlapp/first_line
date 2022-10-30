
from django.urls import path

from .views import TypeOfTournamentViewSet


urlpatterns = [
    path("api/v1/type-of-tournaments",
         TypeOfTournamentViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/type-of-tournaments/<int:pk>',
         TypeOfTournamentViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
