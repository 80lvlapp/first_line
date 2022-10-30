
from django.urls import path

from .views import CategoryViewSet


urlpatterns = [
   path("api/v1/category",
         CategoryViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/category/<int:pk>',
         CategoryViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]