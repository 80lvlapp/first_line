
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from .models import CategoryValueModel
from rest_framework.response import Response
from .category_value_serializers import CategoryValueSerializer,  CategoryValueCreateSerializer


class CategoryValueViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs) -> Response:

        queryset = CategoryValueModel.objects.all()
        serializer = CategoryValueSerializer(queryset, many=True)
        return Response({"status": "OK", "data": serializer.data})

    def create(self, request, *args, **kwargs):

        serializer = CategoryValueCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = CategoryValueModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = CategoryValueSerializer(element)
        return Response({"status": "ok", "data": serializer.data})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(CategoryValueModel.objects.all(), pk=pk)
        serializer = CategoryValueCreateSerializer(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(CategoryValueModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": 'OK'})
