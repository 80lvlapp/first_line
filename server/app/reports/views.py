from dataclasses import fields
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize

from api.sportsman_info.models import SportsmanInfoModel
from api.tournament_info.models import TournamentInfoModel
from django.db.models import Sum

from api.tournament_info.tournament_info_serializers import TournamentInfoReportSerializers, TournamentSportsmanReportInfoReportSerializers


class SportsmanPointsReportViewSet(viewsets.ModelViewSet):
    def list(self, request: Request, *args, **kwargs) -> Response:
        print(f"{request.query_params}")
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        sport_school_pk = request.query_params.get("sport_school_pk")
        queryset = TournamentInfoModel.objects.filter(
            sportsman__pk__in=SportsmanInfoModel.objects.values("sportsman").filter(
                sport_school__pk=sport_school_pk)).annotate(
            Sum("points")).order_by(
            "-points__sum")

        if start_date is not None:
            if start_date != "":
                queryset = queryset.filter(period__gte=start_date)
        if end_date is not None:
            if end_date != "":
                queryset = queryset.filter(period__lte=end_date)
        print(f"{queryset}")
        serializer = TournamentInfoReportSerializers(queryset, many=True)
        return Response({"status": "OK", "data": serializer.data})


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
        #serializer = TournamentSportsmanReportInfoReportSerializers(queryset1, many=True)
        #return Response({"status": "OK", "data": serializer.data})
        my_list = []
        for element in queryset1:
            e2_s = TournamentSportsmanReportInfoReportSerializers(element)
            my_list.append(e2_s)
            print(e2_s)
        # print("=============================")
        # for element in queryset2:
        #     e1_s = TypeOfTournametSerializers(element)
        #     print(e1_s)
        return HttpResponse(qs_json, content_type='application/json', headers={"Access-Control-Allow-Origin": "*"})
        #return HttpResponse(TournamentSportsmanReportInfoReportSerializers(queryset1[0]).data, content_type='application/json')
