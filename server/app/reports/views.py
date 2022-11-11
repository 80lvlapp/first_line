
from rest_framework import viewsets

from rest_framework.request import Request


from django.http import JsonResponse

from api.sportsman_info.models import SportsmanInfoModel
from api.tournament_info.models import TournamentInfoModel
from django.db.models import Sum

from api.sportsman.sportsman_serializers import SportsmanSerializers
from api.tournament.tournament_serializers import TournamentSerializers


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
    def list(self, request: Request, *args, **kwargs) -> JsonResponse:
        print(f"{request.query_params}")
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        sportsman_id = request.query_params.get("sportsman_id")

        queryset = TournamentInfoModel.objects.all()
        qs1 = TournamentInfoModel.objects.values("sportsman").annotate(points=Sum("points")).order_by("-points")
        if start_date is not None:
            if start_date != "":
                queryset = queryset.filter(period__gte=start_date)
        if end_date is not None:
            if end_date != "":
                queryset = queryset.filter(period__lte=end_date)

        if sportsman_id is not None:
            if sportsman_id != "":
                sportsman_id = int(sportsman_id)
                queryset = queryset.filter(sportsman__id__exact=sportsman_id)

        
        print(f"[TournamentsSportsmenReportViewSet]: QA1 {list(qs1)}")
        print(f"[TournamentsSportsmenReportViewSet]: QS {list(queryset)}")
        #Получаем уникальных спортсменов
        sportsman_set = set()
        for item in list(qs1):
            for item1 in list(queryset):
                if(item1.sportsman.id == item["sportsman"]):
                    sportsman_set.add(item1.sportsman) 
        print(f"[TournamentsSportsmenReportViewSet]: ${sportsman_set}")

        json_qs = []
        n = 1 
        for sportsman_item in list(sportsman_set):
            sportsman_serializer = SportsmanSerializers(sportsman_item)
            tournament_json = []
            points = 0
            for item in list(queryset):
                if (sportsman_item.id == item.sportsman.id):
                    tournament_serializer = TournamentSerializers(item.tournament)
                    tournament_json.append({"tournament": tournament_serializer.data, "point": item.points})
                    points += item.points
            json_element = {"sportsman": sportsman_serializer.data,"place": n, "points": points, "tournaments": tournament_json}        
            json_qs.append(json_element)
            n += 1
        return JsonResponse(json_qs, safe = False , headers={"Access-Control-Allow-Origin": "*"})
        
