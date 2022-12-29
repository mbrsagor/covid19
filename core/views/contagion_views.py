from core.models.contagion import *
from core.serializers.contagion_serializer import *
# from hospital.permissions.permissions import PermissionHelperMixin

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10


class LocationApiView(APIView):

    def get(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LocationUpdateDeleteView(APIView):

    def put(self, request, id):
        queryset = get_object_or_404(Location, id=id)
        serializer = LocationSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = get_object_or_404(Location, id=id)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class DiseaseViewSet(ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [IsAuthenticated]


class ContagionApiView(APIView):

    def get(self, request):
        queryset = Contagion.objects.all()
        serializer = ContagionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContagionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ContagionUpdateDeleteView(APIView):

    def get(self, request, id):
        queryset = get_object_or_404(Contagion, id=id)
        serializer = ContagionSerializer(queryset).data
        return Response(serializer, status=HTTP_200_OK)

    def put(self, request, id):
        queryset = get_object_or_404(Contagion, id=id)
        serializer = ContagionSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_204_NO_CONTENT)

    def delete(self, request, id):
        queryset = get_object_or_404(Contagion, id=id)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class HelpViewSet(ModelViewSet):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


class HospitalViewSet(ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    pagination_class = StandardResultsSetPagination
