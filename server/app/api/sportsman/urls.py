
from django.urls import path

from .views import SportsmanViewSet


urlpatterns = [
    path("api/v1/sportsmen",
         SportsmanViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/sportsmen/<int:pk>',
         SportsmanViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
