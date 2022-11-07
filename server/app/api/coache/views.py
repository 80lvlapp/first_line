from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import CoacheModel
from .coache_serializers import CoacheSerializers


class CoacheViewSet(viewsets.ModelViewSet):

    serializer_class = CoacheSerializers

    def get_queryset(self):
        return CoacheModel.objects.all()

    def list(self, request, *args, **kwargs) -> Response:

        queryset = CoacheModel.objects.all().order_by('name')
        search_name = request.query_params.get('name')
        if search_name is not None:
            queryset = queryset.filter(name__icontains=search_name)
        serializer = CoacheSerializers(queryset, many=True)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def create(self, request, *args, **kwargs):
        serializer = CoacheSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers={"Access-Control-Allow-Origin": "*"})

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = CoacheModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = CoacheSerializers(element)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(CoacheModel.objects.all(), pk=pk)
        serializer = CoacheSerializers(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": False}, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:
        element = get_object_or_404(CoacheModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": True})
