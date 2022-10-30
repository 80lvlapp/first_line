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
from django.urls import path, include


MAIN_URL = "fist-line/"

urlpatterns = [
    path('admin/', admin.site.urls),

    path(MAIN_URL, include("api.category.urls")),
    path(MAIN_URL, include("api.coache.urls")),
    path(MAIN_URL, include("api.sport_school.urls")),
    path(MAIN_URL, include("api.type_of_tournament.urls")),
    path(MAIN_URL, include("api.category_value.urls")),
    path(MAIN_URL, include("api.sportsman.urls")),
    path(MAIN_URL, include("api.tournament.urls")),
    path(MAIN_URL, include("api.score_scale.urls")),
    path(MAIN_URL, include("api.sportsman_info.urls")),
    path(MAIN_URL, include("api.tournament_info.urls")),
    path(MAIN_URL, include("api.tournament_info.urls")),
    path(MAIN_URL, include("reports.urls")),
]
