from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['token'] = str(refresh.access_token)
        return data

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = HrEmployee
        fields = ['id']

def get_date(id):
    try:
        return TrxFleetWorkingVehicleDriver.objects.get(pk=id).start_date
    except:
        return None

def get_driver(id):
    try:
        return TrxFleetDriver.objects.get(pk=id).driver_id
    except:
        return None

class VehicleFleetSerializers(serializers.ModelSerializer):
    vehicleBrand = serializers.ReadOnlyField(source='brand.name')
    vehicleType = serializers.ReadOnlyField(source='category.name')
    vehicleCategoryID = serializers.ReadOnlyField(source='category.id')
    driverID = serializers.ReadOnlyField(source='driver.id')
    employeeID = serializers.ReadOnlyField(source='driver_employee.id')
    employeeName = serializers.ReadOnlyField(source='driver_employee.name')
    class Meta :
        model = FleetVehicle
        fields = ['id','name','driverID','employeeID','employeeName','vehicleBrand','vehicleType', 'vehicleCategoryID',]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        short = FleetVehicleVehicleTagRel.objects.get(pk=instance)
        date = get_date(instance.id)
        driverID= get_driver(instance.id)
        shortname =short.tag.name
        odo = FleetVehicleOdometer.objects.filter(vehicle=instance.id)
        data['vehicleID'] = data.pop('id')
        data['vehicleName'] = data.pop('name')
        data['vehicleShotrtName'] = shortname['en_US']
        data['date'] =  date
        data['driverID'] =  driverID
        data['vehicleDescription'] = {
            "model_id": instance.model.id,
			"model_name": instance.model.name,
			"brand_id": instance.brand.id,
			"brand_name": instance.brand.name,
			"category_id": instance.category.id,
			"category_name": instance.category.name,
			"license_plate": instance.license_plate,
			"vin_sn": instance.vin_sn,
			"active": instance.active,
			"location": instance.location,
			"model_year": instance.model_year,
			"fuel_type": instance.fuel_type,
			"vehicle_type": instance.model.name,
            "odometer_unit": odo
        }
        return data   

      
class TrxFleetWorkingVehicleDriverSerializers(serializers.ModelSerializer):
    # vehicleParent = VehicleFleetSerializers(many=True, read_only=True)
    class Meta:
        model = TrxFleetWorkingVehicleDriver
        fields = '__all__'
        
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        vehicle = FleetVehicle.objects.get(id=instance.vehicle_id)
        short = FleetVehicleVehicleTagRel.objects.get(pk=vehicle.id)
        date = get_date(vehicle.id)
        driverID= get_driver(vehicle.id)
        shortname =short.tag.name
        print(vehicle.model.name)
        vehicle_type = vehicle.model.name
        brand_name = vehicle.brand.name
        data['vehicleID'] = vehicle.id
        data['vehicleName'] = vehicle.name
        data['vehicleShotrtName'] = shortname['en_US']
        data['date'] =  date
        data['driverID'] =  driverID
        data['vehicle_type']= vehicle_type
        data['brand_name'] = brand_name
        data['vehicleDescription'] = []
        del data['id']
        del data['vehicle_id']
        del data['drive_id']
        del data['parent_id']
        del data['start_date']
        del data['start_time']
        del data['end_date']
        del data['end_time']
        del data['order']
        return data
    
    
class TrxFleetLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrxFleetLookup
        fields = '__all__'
