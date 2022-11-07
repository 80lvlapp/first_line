from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import TypeOfTournamentModel
from .type_of_tournamet_serializers import TypeOfTournametSerializers


class TypeOfTournamentViewSet(viewsets.ModelViewSet):

    serializer_class = TypeOfTournametSerializers

    def get_queryset(self):
        return TypeOfTournamentModel.objects.all()

    def list(self, request, *args, **kwargs) -> Response:

        queryset = TypeOfTournamentModel.objects.all().order_by('name')
        search_name = request.query_params.get('name')
        if search_name is not None:
            queryset = queryset.filter(name__icontains=search_name)
        serializer = TypeOfTournametSerializers(queryset, many=True)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def create(self, request, *args, **kwargs) -> Response:
        serializer = TypeOfTournametSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = TypeOfTournamentModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = TypeOfTournametSerializers(element)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(TypeOfTournamentModel.objects.all(), pk=pk)
        serializer = TypeOfTournametSerializers(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": False}, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:
        element = get_object_or_404(TypeOfTournamentModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": True}, headers={"Access-Control-Allow-Origin": "*"})
