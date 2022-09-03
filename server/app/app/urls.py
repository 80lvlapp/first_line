"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.category.views import CategoryViewSet
from api.coache.views import CoacheViewSet
from api.sport_school.views import SportSchoolViewSet
from api.type_of_tournament.views import TypeOfTournamentViewSet
from api.category_value.views import CategoryValueViewSet
from api.sportsman.views import SportsmanViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1/category",
         CategoryViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/category/<int:pk>',
         CategoryViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),

    path("api/v1/coach",
         CoacheViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/coach/<int:pk>',
         CoacheViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),

    path("api/v1/schools",
         SportSchoolViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/schools/<int:pk>',
         SportSchoolViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),

    path("api/v1/type-of-tournaments",
         TypeOfTournamentViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/type-of-tournaments/<int:pk>',
         TypeOfTournamentViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),

    path("api/v1/value-category",
         CategoryValueViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/value-category/<int:pk>',
         CategoryValueViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),

    path("api/v1/sportsmen",
         SportsmanViewSet.as_view({'get': "list", "post": "create"})),
    path('api/v1/sportsmen/<int:pk>',
         SportsmanViewSet.as_view({"get": "retrieve", "put": 'update', "delete": "destroy"})),
]
