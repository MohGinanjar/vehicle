from django.shortcuts import render
from rest_framework import response,status,generics
from .serilazers import *
from .models import FleetVehicle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

class ListFleetVehicle(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
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

def get_vehicle(pk, driver):
    try:
        return driver.objects.get(pk=pk)
    except:
        return None


class FleetVehicleDelete(generics.GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = FleetVehicle.objects.all().order_by('-id')
    serializer_class = FleetVehicleSerializers
    
    
    
    
    
    def delete(self, request):
        vehicleID = request.query_params.get('vehicleID', None)
        driverID = request.query_params.get('driverID', None) 
        veh = FleetVehicle.objects.get(pk=vehicleID)
        return Response({'data':'ada'})
        # try:
        #     vehicles = FleetVehicle.objects.get(pk=vehicleID)
        #     Response({'data':'ada'})
        # except:
        #     Response({"status": "failed", "message": f"Vehicle with Id: {vehicleID} not found"}, status=status.HTTP_404_NOT_FOUND)
        # # print(veh)
        # if FleetVehicle.objects.get(pk=vehicleID).DoesNotExist:     
        #     # vehicle = get_vehicle(FleetVehicle, vehicleID)
        #     # driver = get_vehicle(VehicleEmployee, driverID)
        #     # if vehicle  == None:
        #     #     return Response({"status": "failed", "message": f"Vehicle with Id: {vehicleID} not found"}, status=status.HTTP_404_NOT_FOUND)
        #     # else :
        #     #     vehicles = FleetVehicle.objects.get(pk=vehicleID)
        #     #     driver = VehicleEmployee.objects.get(pk=vehicleID)
        #     #     vehicles.delete()
        #     #     driver.delete()
        #     return Response({'data':'tidak ada'})
        # else:
        #     return Response({'data':'ada'})