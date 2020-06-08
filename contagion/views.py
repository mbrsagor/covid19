from .models import *
from .serializers import *

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet


class CountryApiView(APIView):

    def get(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, HTTP_201_CREATED)
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class CountryUpdateDeleteView(APIView):

    def put(self, request, id):
        queryset = get_object_or_404(Country, id=id)
        serializer = CountrySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = get_object_or_404(Country, id=id)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class DiseaseViewSet(ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


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
