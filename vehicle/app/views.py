from django.shortcuts import render
from rest_framework import response,status,generics
from .serilazers import *
from .models import FleetVehicle
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ListFleetVehicle(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = FleetVehicle.objects.all().order_by('-id')
    serializer_class = FleetVehicleSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
