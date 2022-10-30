
from django.urls import path

from .views import ScoreScaleViewSet


urlpatterns = [
   path("api/v1/score-scale",
         ScoreScaleViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/score-scale/<int:pk>',
         ScoreScaleViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]