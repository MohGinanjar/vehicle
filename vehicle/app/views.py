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
class TrxFleetWorkingVehicleDriverView(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = TrxFleetWorkingVehicleDriver.objects.all().order_by('id')
    serializer_class = TrxFleetWorkingVehicleDriverSerializers
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['vehicle_id', 'drive_id', 'start_date', 'end_date']
    
    def list(self, request, *args, **kwargs):
        vehicle_id = self.request.query_params.get('vehicleID', None)
        drive_id = self.request.query_params.get('driverID', None)
        date = self.request.query_params.get('date', None)
        trx = TrxFleetWorkingVehicleDriver.objects.filter(vehicle_id=vehicle_id)
        if trx.exists():
            serializer = self.get_serializer(trx, many=True)
            print(serializer.data)
            
            return JsonResponse({
            'status':"ok",
            'message': 'sucsess',
            'jsonResult':{
                'vehicleParent':serializer.data,
                'driver':[]
            }
            })
        else:
            return JsonResponse({
            'error':"10007",
            'message': 'Record Does Not Exist. Please Validate Your Input.',})


### 1.1.5        
class deleteVehicleDriver(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = TrxFleetWorkingVehicleDriver.objects.all().order_by('id')
    serializer_class = TrxFleetWorkingVehicleDriverSerializers
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['vehicle_id', 'drive_id', 'start_date', 'end_date']
          
    def delete(self, request):
        vehicle_id = self.request.query_params.get('vehicleID', None)
        driver_id = self.request.query_params.get('driverID', None)
        date = self.request.query_params.get('date', None)
        trx = TrxFleetWorkingVehicleDriver
        if vehicle_id and driver_id is not None :
            if trx.objects.filter(vehicle_id=vehicle_id).exists():
              tr = trx.objects.filter(vehicle_id=vehicle_id, start_date=date, end_date=date)
              serializer = self.get_serializer(tr, many=True)
              return JsonResponse({
                'status':"ok",
                'message': 'sucsess',
                'jsonResult':{
                    'vehicleParent':serializer.data,
                    'driver':[]
                }
                }) 
            else:
                return JsonResponse({
                'error':"10007",
                'message': 'Record Does Not Exist. Please Validate Your Input.',}) 
        elif driver_id is not None:
            if trx.objects.filter(vehicle_id=vehicle_id, driver_id=driver_id).exists():
                tr = trx.objects.filter(vehicle_id=vehicle_id, start_date=date, end_date=date)
                serializer = self.get_serializer(tr, many=True)
                return JsonResponse({
                    'status':"ok",
                    'message': 'sucsess',
                    'jsonResult':{
                        'vehicleParent':serializer.data,
                        'driver':[]
                    }
                    })
            else:  
                return JsonResponse({
                'error':"10007",
                'message': 'Record Does Not Exist. Please Validate Your Input.',})
        else:
            return JsonResponse({
                'error':"10007",
                'message': 'Record Does Not Exist. Please Validate Your Input.',})
            
            
            
class viewRotation(generics.ListCreateAPIView):
    queryset = TrxFleetLookup.objects.all().order_by('id')
    serializer_class = TrxFleetLookupSerializer
    
    def post(self, request, *args, **kwargs):
        
        serializer = TrxFleetLookupSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            serializer = TrxFleetLookupSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)