from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import ScoreScaleModel
from .score_scale_serializers import ScoreScaleSerializers, ScoreScaleCreateSerializers


class ScoreScaleViewSet(viewsets.ModelViewSet):

    serializer_class = ScoreScaleSerializers

    def get_queryset(self):
        return ScoreScaleModel.objects.all()

    def list(self, request, *args, **kwargs) -> Response:

        queryset = ScoreScaleModel.objects.all()

        serializer = ScoreScaleSerializers(queryset, many=True)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def create(self, request, *args, **kwargs):
        serializer = ScoreScaleCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = ScoreScaleModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = ScoreScaleSerializers(element)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(ScoreScaleModel.objects.all(), pk=pk)
        serializer = ScoreScaleCreateSerializers(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST, headers={"Access-Control-Allow-Origin": "*"})

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:
        element = get_object_or_404(ScoreScaleModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": True}, headers={"Access-Control-Allow-Origin": "*"})
