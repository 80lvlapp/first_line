from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
# from .models import SportsmanPointsReport
# from .reports_serializers import SportsmanPointsReportSerializers
from api.sportsman_info.models import SportsmanInfoModel
from api.tournament_info.models import TournamentInfoModel
from django.db.models import Sum

# Create your views here.
from api.tournament_info.tournament_info_serializers import TournamentInfoReportSerializers


class SportsmanPointsReportViewSet(viewsets.ModelViewSet):
    def list(self, request: Request, *args, **kwargs) -> Response:
        print(f"{request.query_params}")
        startDate = request.query_params.get('startDate')
        endDate = request.query_params.get('endDate')
        sport_school_pk = request.query_params.get("sport_school_pk")
        queryset = TournamentInfoModel.objects.filter(
            sportsman__pk__in=SportsmanInfoModel.objects.values("sportsman").filter(
                sport_school__pk=sport_school_pk)).annotate(
            Sum("points")).order_by(
            "-points__sum")

        if startDate is not None:
            queryset = queryset.filter(period__gte=startDate)
        if endDate is not None:
            queryset = queryset.filter(period__lte=endDate)
        print(f"{queryset}")
        serializer = TournamentInfoReportSerializers(queryset, many=True)
        return Response({"status": "OK", "data": serializer.data})
