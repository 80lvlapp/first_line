
from django.urls import path

from .views import SportSchoolViewSet


urlpatterns = [
    path("api/v1/schools",
         SportSchoolViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/schools/<int:pk>',
         SportSchoolViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
