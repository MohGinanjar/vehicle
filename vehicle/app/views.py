from django.shortcuts import render
from rest_framework import response,status,generics
from .serilazers import *
from .models import FleetVehicle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin
from django.shortcuts import get_object_or_404
# fro import MyTokenObtainPairSerializer, LoginSerializer
from .serilazers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

### 1.1.3
class ListFleetVehicle(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = FleetVehicle.objects.all().order_by('id')
    serializer_class = VehicleFleetSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        drivers = queryset.values('driver')
        print(drivers)
        
        # driver = HrEmployee.objects.filter(vehicle__in=drivers)
        # serializer_driver = DriverSerializer(driver, many=True)
        serializer = self.get_serializer(queryset, many=True)
        total = queryset.count()
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        return Response({
            "success": True,
            "errors": "string",
            "messages": "string",
            "recordInfo": {
                "totalData": total,
                "currentPage": page_num,
                "totalPage": limit_num
            },
            'jsonResult':{
                'vehicle': serializer.data,
                'driver':drivers
            }
        })

#### 1.1.4

class TrxFleetWorkingVehicleDriverView(generics.GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = TrxFleetWorkingVehicleDriver.objects.all().order_by('id')
    serializer_class = TrxFleetWorkingVehicleDriverSerializers
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['vehicle_id', 'drive_id', 'start_date', 'end_date']
    
    def get(self, request):
        vehicle_id = self.request.query_params.get('vehicleID', None)
        drive_id = self.request.query_params.get('driverID', None)
        date = self.request.query_params.get('date', None)
        trx = TrxFleetWorkingVehicleDriver.objects.filter(vehicle_id=vehicle_id, drive_id=drive_id, start_date=date ,end_date=date)
        if trx.exists():
            if trx[0].order == 0:
                return JsonResponse({
                'error':"10014",
                'message': 'Record cannot be processed. Please Validate Your Input.',})
        else:   
            return JsonResponse({
            'error':"10007",
            'message': 'Record Does Not Exist. Please Validate Your Input.',})
     ### 1.1.5       
    def delete(self, request):
        vehicle_id = self.request.query_params.get('vehicleID', None)
        print(vehicle_id)
        # drive_id = self.request.query_params.get('driverID', None)
        # date = self.request.query_params.get('date', None)
        # trx = TrxFleetWorkingVehicleDriver.objects.filter(vehicle_id=vehicle_id, drive_id=drive_id, start_date=date ,end_date=date)
        # if trx.exists():
        #     if trx[0].order == 0:
        #         return JsonResponse({
        #         'error':"10014",
        #         'message': 'Record cannot be processed. Please Validate Your Input.',})
        # else:   
        return JsonResponse({
        'error':"10007",
        'message': 'Record Does Not Exist. Please Validate Your Input.',})