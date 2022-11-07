from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import SportsmanInfoModel
from .sportsman_info_serializers import SportsmanInfoSerializers, SportsmanInfoCreateSerializers


class SportsmanInfoViewSet(viewsets.ModelViewSet):

    serializer_class = SportsmanInfoSerializers

    def get_queryset(self):
        return SportsmanInfoModel.objects.all()

    def list(self, request, *args, **kwargs) -> Response:

        queryset = SportsmanInfoModel.objects.all()

        serializer = SportsmanInfoSerializers(queryset, many=True)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def create(self, request, *args, **kwargs):
        serializer = SportsmanInfoCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = SportsmanInfoModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = SportsmanInfoSerializers(element)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(SportsmanInfoModel.objects.all(), pk=pk)
        serializer = SportsmanInfoCreateSerializers(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": False}, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:
        element = get_object_or_404(SportsmanInfoModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": True}, headers={"Access-Control-Allow-Origin": "*"})
