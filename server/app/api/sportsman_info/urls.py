
from django.urls import path

from .views import SportsmanInfoViewSet


urlpatterns = [
    path("api/v1/sportsman-info",
         SportsmanInfoViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/sportsman-info/<int:pk>',
         SportsmanInfoViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),

]
