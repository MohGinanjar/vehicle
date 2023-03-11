from django.shortcuts import render
from rest_framework import response,status,generics
from .serilazers import *
from .models import FleetVehicle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin
from django.shortcuts import get_object_or_404
from dashboard.serializers import MyTokenObtainPairSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class LoginAuthView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ListFleetVehicleCategory(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FleetVehicleModelCategory.objects.all().order_by('-id')
    serializer_class = VehicleCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    

class ListVehicleRotation(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FleetVehicle.objects.all().order_by('-id')
    serializer_class = FleetVehicleSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    


class ListFleetVehicle(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FleetVehicle.objects.all().order_by('-id')
    serializer_class = FleetVehicleSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    
    # def get_queryset(self):
    #     vehicles = FleetVehicle.objects.all().order_by('-id')
    #     return vehicles
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        drivers = queryset.values('driver')
        driver = VehicleEmployee.objects.filter(id__in=drivers)
        serializer_driver = DriverSerializer(driver, many=True)
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
                "pageSize": start_num,
                "totalPage": limit_num
            },
            'jsonResult':{
                'vehicle': serializer.data,
                'driver':serializer_driver.data
            }
        })


    
    
class FleetVehicleDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset1 = FleetVehicle.objects.all()
    queryset2 = VehicleEmployee.objects.all()
    serializer_class1 = FleetVehicleSerializers
    serializer_class2 = DriverSerializer
    
    # def destroy(self, request, *args, **kwargs):
    #     vehicleId=request.query_params.get('vehicleID', None)
    #     driverID=request.query_params.get('driverID', None)
    
    def get_vehicle(self, request):
        try:
            vehicleId=request.query_params.get('vehicleID', None)
            return FleetVehicle.objects.get(pk=vehicleId)
        except:
            return None
    
    def get_driver(self, request):
        try:
            vehicleId=request.query_params.get('driverID', None)
            return VehicleEmployee.objects.get(pk=vehicleId)
        except:
            return None
    
    
    def delete(self, request, *args, **kwargs):
        vehicleId=request.query_params.get('vehicleID', None)
        driverID=request.query_params.get('driverID', None)
        note = self.get_vehicle(request=request)
        driver = self.get_driver(request=request)
        if note and driver != None:
            note.delete()
            driver.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"status": "fail", "message": f"Vehicle with Id: {vehicleId} and Driver {driverID} not found"}, status=status.HTTP_404_NOT_FOUND)


class FleetVehicleCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FleetVehicle.objects.all()
    serializer_class = VehicleFleetSerializers
    

class RotationVehicleCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = VehicleRotation.objects.all()
    serializer_class = RotationSerializers


class TimeSheetCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializers
    
    

class RotationVehicleDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = VehicleRotation.objects.all()
    serializer_class = RotationSerializers
    
    def get_driver(self, request):
        try:
            rotationID=request.query_params.get('rotationID', None)
            return VehicleRotation.objects.get(pk=rotationID)
        except:
            return None
        
    def delete(self, request, *args, **kwargs):
        rotationID=request.query_params.get('rotationID', None)
        driver = self.get_driver(request=request)
        if driver != None:
            driver.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"status": "fail", "message": f"Vehicle Rotation with Id: {rotationID}  not found"}, status=status.HTTP_404_NOT_FOUND)