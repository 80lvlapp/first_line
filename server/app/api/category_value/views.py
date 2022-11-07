
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from .models import CategoryValueModel
from rest_framework.response import Response
from .category_value_serializers import CategoryValueSerializer,  CategoryValueCreateSerializer


class CategoryValueViewSet(viewsets.ModelViewSet):

    serializer_class = CategoryValueSerializer
    

    def get_queryset(self):
        return CategoryValueModel.objects.all()
    def list(self, request, *args, **kwargs) -> Response:

        queryset = CategoryValueModel.objects.all()
        serializer = CategoryValueSerializer(queryset, many=True)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def create(self, request, *args, **kwargs):

        serializer = CategoryValueCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs) -> Response:

        queryset = CategoryValueModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = CategoryValueSerializer(element)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def update(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(CategoryValueModel.objects.all(), pk=pk)
        serializer = CategoryValueCreateSerializer(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs) -> Response:

        element = get_object_or_404(CategoryValueModel.objects.all(), pk=pk)
        element.delete()
        return Response({"message": True})
