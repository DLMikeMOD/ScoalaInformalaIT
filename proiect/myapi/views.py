from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from app1.models import Location
from myapi.serializers import LocationSerializers


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializers
