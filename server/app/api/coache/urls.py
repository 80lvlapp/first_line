
from django.urls import path

from .views import CoacheViewSet


urlpatterns = [
    path("api/v1/coach",
         CoacheViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/coach/<int:pk>',
         CoacheViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
