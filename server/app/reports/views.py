
from rest_framework import viewsets

from rest_framework.request import Request


from django.http import JsonResponse

from api.sportsman_info.models import SportsmanInfoModel
from api.tournament_info.models import TournamentInfoModel
from django.db.models import Sum, Q

from api.sportsman.sportsman_serializers import SportsmanSerializers
from api.tournament.tournament_serializers import TournamentSerializers
from api.category_value.category_value_serializers import CategoryValueCreateSerializer


class SportsmanPointsReportViewSet(viewsets.ModelViewSet):
    def list(self, request: Request, *args, **kwargs):
        print(f"{request.query_params}")
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        sport_school_pk = request.query_params.get("sport_school_pk")
        queryset = TournamentInfoModel.objects.values_list("sportsman", "sportsman__name", "sportsman__gender", "sportsman__date_birth").filter(sportsman__pk__in=SportsmanInfoModel.objects.filter(sport_school__pk__exact=sport_school_pk)).annotate(points=Sum("points")).order_by("-points")
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
            id = item[0]
            name = item[1]
            gender = item[2]
            date_birth = item[3]
            points = float(item[4])
            json_element = {
                "points": points,
                "place": n,
                "sportsman": {"id": id, "name": name, "gender": gender, "date_birth": date_birth}
            }
            json_qs.append(json_element)
            n += 1
        
        return JsonResponse(json_qs, safe = False , headers={"Access-Control-Allow-Origin": "*"})


class TournamentsSportsmenReportViewSet(viewsets.ModelViewSet):
    def list(self, request: Request, *args, **kwargs) -> JsonResponse:
        print(f"{request.query_params}")
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        sportsman_id = request.query_params.get("sportsman_id")

        queryset = TournamentInfoModel.objects.all()
       
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

        if start_date is not None and end_date is None and sportsman_id is None:
            pass        

        qs1 = queryset.values("sportsman").annotate(points=Sum("points")).order_by("-points")
        qs_tournament = queryset.values("sportsman", "tournament").annotate(points=Sum("points")).order_by("-points")
        print(f"[TournamentsSportsmenReportViewSet]: QA1 {list(qs1)}")
        print(f"[TournamentsSportsmenReportViewSet]: QS {list(queryset)}")
        print(f"[TournamentsSportsmenReportViewSet]: qs_tournament {list(qs_tournament)}")
       
        json_qs = []

        for group1 in list(qs1):
            queryset1 = queryset.filter(sportsman__id__exact=group1['sportsman'])
            if (queryset1.count() > 0):
                sportsman_serializer = SportsmanSerializers(queryset1[0].sportsman)
                tournament_json = []
                for group2 in list(qs_tournament):
                    if group2["sportsman"] == group1["sportsman"]:
                        queryset2 = queryset.filter(Q(sportsman__id__exact=group1['sportsman']) & Q(tournament__id__exact=group2['tournament']))
                        if queryset2.count() > 0:
                            tournament_serializer = TournamentSerializers(queryset2[0].tournament)
                            points = 0
                            for item in list(queryset2):
                                points += item.points
                            tournament_json.append({"tournament":tournament_serializer.data, "point": points})
                        
                        
                json_element = {"sportsman": sportsman_serializer.data, "points": group1['points'], "tournaments": tournament_json}
                json_qs.append(json_element)

        return JsonResponse(json_qs, safe = False , headers={"Access-Control-Allow-Origin": "*"})


class TournamentsSportsmenCategoryReportViewSet(viewsets.ModelViewSet):
    def list(self, request: Request, *args, **kwargs) -> JsonResponse:
        print(f"{request.query_params}")
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        sportsman_id = request.query_params.get("sportsman_id")
        tournament_id = request.query_params.get("tournament_id")
        queryset = TournamentInfoModel.objects.all()
      
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

        if tournament_id is not None:
            if tournament_id != "":
                tournament_id = int(tournament_id)
                queryset = queryset.filter(tournament__id__exact=tournament_id)

        qs1 = queryset.values("sportsman").annotate(points=Sum("points")).order_by("-points")
        qs2 = queryset.values("sportsman", 'tournament').annotate(points=Sum("points")).order_by("-points")        
        qs3 = queryset.values("sportsman", 'tournament', "category_value").annotate(points=Sum("points")).order_by("-points")

        
        json_qs = []
        for group1 in list(qs1):
            queryset1 = queryset.filter(sportsman__id__exact=group1['sportsman'])
            if (queryset1.count() > 0):
                sportsman_serializer = SportsmanSerializers(queryset1[0].sportsman)
                tournament_json = []
                
                for group2 in list(qs2):
                    if group2["sportsman"] == group1["sportsman"]:
                        queryset2 = queryset.filter(Q(sportsman__id__exact=group1['sportsman']) & Q(tournament__id__exact=group2['tournament']))
                        if queryset2.count() > 0:
                            tournament_serializer = TournamentSerializers(queryset2[0].tournament)
                            category_value_json = []
                            tournament_point = 0;
                            for group3 in list(qs3):
                                if group3["sportsman"] == group1["sportsman"] and group2['tournament'] == group3['tournament']:
                                    queryset3 = queryset.filter(Q(sportsman__id__exact=group1['sportsman']) & Q(tournament__id__exact=group2['tournament']) & Q(category_value__id__exact=group3['category_value']))    
                                    if queryset3.count() > 0:
                                        
                                        point_category_value = 0;
                                        for item in list(queryset3):
                                            point_category_value += item.points
                                            tournament_point +=item.points
                                        category_value_json.append({"category": CategoryValueCreateSerializer(queryset3[0].category_value).data, "point": point_category_value})                                        
                            
                            tournament_json.append({"tournament":tournament_serializer.data, "point": tournament_point, "categores": category_value_json})
                        
                        
                json_element = {"sportsman": sportsman_serializer.data, "points": group1['points'], "tournaments": tournament_json}
                json_qs.append(json_element)

        return JsonResponse(json_qs, safe = False , headers={"Access-Control-Allow-Origin": "*"})
           

        



        
