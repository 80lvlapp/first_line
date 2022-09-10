from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import TournamentInfoModel
from .tournament_info_serializers import TournamentInfoSerializers, TournamentInfoCreateSerializers


class TournamentInfoViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs) -> Response:
        queryset = TournamentInfoModel.objects.all()
        startDate = request.query_params.get('startDate')
        endDate = request.query_params.get('endDate')
        idSchool = request.query_params.get('idSchool')
        if startDate is not None:
            queryset.filter(period__gte=startDate)
        if endDate is not None:
            queryset.filter(period__lte=endDate)
        # if idSchool is not None:
        #     queryset.filter
        serializer = TournamentInfoSerializers(queryset, many=True)
        return Response({"status": "OK", "data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = TournamentInfoCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = TournamentInfoModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = TournamentInfoSerializers(element)
        return Response({"status": "ok", "data": serializer.data})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(TournamentInfoModel.objects.all(), pk=pk)
        serializer = TournamentInfoCreateSerializers(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:
        element = get_object_or_404(TournamentInfoModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": 'OK'})
