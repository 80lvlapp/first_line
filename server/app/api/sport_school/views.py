from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import SportSchoolModel
from .sport_school_serializers import SportSchoolSerializers


class SportSchoolViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs) -> Response:

        queryset = SportSchoolModel.objects.all().order_by('name')
        search_name = request.query_params.get('name')
        if search_name is not None:
            queryset = queryset.filter(name__icontains=search_name)
        serializer = SportSchoolSerializers(queryset, many=True)
        # return Response({"status": "OK", "data": serializer.data}) 
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def create(self, request, *args, **kwargs)-> Response:
        serializer = SportSchoolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = SportSchoolModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = SportSchoolSerializers(element)
        return Response({"status": "ok", "data": serializer.data})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(SportSchoolModel.objects.all(), pk=pk)
        serializer = SportSchoolSerializers(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:
        element = get_object_or_404(SportSchoolModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": 'OK'})
