from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import SportsmanModel
from .sportsman_serializers import SportsmanSerializers


class SportsmanViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs) -> Response:

        queryset = SportsmanModel.objects.all().order_by('name')
        search_name = request.query_params.get('name')
        if search_name is not None:
            queryset = queryset.filter(name__icontains=search_name)
        serializer = SportsmanSerializers(queryset, many=True)
        return Response({"status": "OK", "data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = SportsmanSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = SportsmanModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = SportsmanSerializers(element)
        return Response({"status": "ok", "data": serializer.data})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(SportsmanModel.objects.all(), pk=pk)
        serializer = SportsmanSerializers(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:
        element = get_object_or_404(SportsmanModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": 'OK'})
