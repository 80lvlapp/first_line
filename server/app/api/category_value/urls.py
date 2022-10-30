
from django.urls import path

from .views import CategoryValueViewSet


urlpatterns = [
    path("api/v1/value-category",
         CategoryValueViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/value-category/<int:pk>',
         CategoryValueViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
