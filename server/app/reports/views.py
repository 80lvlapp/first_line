
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import  HttpResponse
from django.core.serializers import serialize
from django.http import JsonResponse

from api.sportsman_info.models import SportsmanInfoModel
from api.tournament_info.models import TournamentInfoModel
from django.db.models import Sum

from api.tournament_info.tournament_info_serializers import TournamentSportsmanReportInfoReportSerializers


class SportsmanPointsReportViewSet(viewsets.ModelViewSet):
    def list(self, request: Request, *args, **kwargs):
        print(f"{request.query_params}")
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        sport_school_pk = request.query_params.get("sport_school_pk")
        queryset = TournamentInfoModel.objects.values_list("period", "sportsman", "sportsman__name", "sportsman__gender", "sportsman__date_birth").filter(sportsman__pk__in=SportsmanInfoModel.objects.filter(sport_school__pk__exact=sport_school_pk)).annotate(points=Sum("points")).order_by("-points")
        print(f"[QS] ${queryset}")
        if start_date is not None:
            if start_date != "":
                queryset = queryset.filter(period__gte=start_date)
        if end_date is not None:
            if end_date != "":
                queryset = queryset.filter(period__lte=end_date)
        print(f"{queryset}")
        json_qs = []
        n = 1
        for item in list(queryset):
            period = item[0]
            id = item[1]
            name = item[2]
            gender = item[3]
            date_birth = item[4]
            points = float(item[5])
            json_element = {
                "period": period,
                "points": points,
                "place": n,
                "sportsman": {"id": id, "name": name, "gender": gender, "date_birth": date_birth}
            }
            json_qs.append(json_element)
            n +=1
        
        return JsonResponse(json_qs, safe = False , headers={"Access-Control-Allow-Origin": "*"})


class TournamentsSportsmenReportViewSet(viewsets.ModelViewSet):
    def list(self, request: Request, *args, **kwargs) -> HttpResponse:
        print(f"{request.query_params}")
        queryset1 = TournamentInfoModel.objects.values("period", "tournament")
        queryset2 = TournamentInfoModel.objects.all()
        print(f"{queryset1}")
        print(f"{queryset2}")
        qs_json = serialize('json', queryset2)
        print(f"{qs_json}")
        print("=============================")
        my_list = []
        for element in queryset1:
            e2_s = TournamentSportsmanReportInfoReportSerializers(element)
            my_list.append(e2_s)
            print(e2_s)
        return HttpResponse(qs_json, content_type='application/json', headers={"Access-Control-Allow-Origin": "*"})
        
