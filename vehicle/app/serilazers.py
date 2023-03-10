from .models import FleetVehicle, VehicleEmployee, FleetVehicleOdometer, FleetVehicleModelCategory
from rest_framework import serializers

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleEmployee
        fields = '__all__'
        


class VehicleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetVehicleModelCategory
        fields = '__all__'

class FleetVehicleSerializers(serializers.ModelSerializer):
    vehicleID = serializers.ReadOnlyField(source='id')
    vehicleCategoryID = serializers.ReadOnlyField(source='vehicle_category.id')
    employeeID = serializers.ReadOnlyField(source='driver.id')
    driverID = serializers.ReadOnlyField(source='driver.id')
    employeeName = serializers.ReadOnlyField(source='driver.employee_name')
    date = serializers.ReadOnlyField(source='driver.date_join')
    category_name = serializers.ReadOnlyField(source='vehicle_category.category_name')
    model_year = serializers.ReadOnlyField(source='vehicle_brand.model_year')
    fuel_type = serializers.ReadOnlyField(source='vehicle_brand.brand.fuel_type')
    brand_name = serializers.ReadOnlyField(source='vehicle_brand.brand.brand_name')
    vehicle_brand = serializers.ReadOnlyField(source='vehicle_brand.brand.brand_name')
    vehicle_type = serializers.ReadOnlyField(source='vehicle_brand.brand.vehicle_type.vehicle_type')
    model_name = serializers.ReadOnlyField(source='vehicle_brand.vehicle_type')
    # #drivers = DriverSerializer(many=False, read_only=True)
    
    class Meta :
        model = FleetVehicle
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        odo = FleetVehicleOdometer.objects.filter(id=data['odomoter']).values('value', 'created_date')
        data['vehicleDescription'] = {
            'category_id':data['vehicle_category'],
            'category_name':data['model_name'],
            'license_plate':data['license_plate'],
            'vin_sn':data['vin_sn'],
            'active':data['active'],
            'location':data['location'],
            'brand_name':data['brand_name'],
            'model_year':data['model_year'],
            'fuel_type':data['fuel_type'],
            'vehicle_type':data['vehicle_type'],
            'odometer':odo
        }
        del data['license_plate']
        del data['vin_sn']
        del data['active']
        del data['location']
        del data['brand_name']
        del data['model_year']
        del data['fuel_type']
        del data['vehicle_type']
        del data['odomoter']
        del data['driver']
        del data['id']
        return data
    

class VehicleFleetSerializers(serializers.ModelSerializer):
    class Meta :
        model = FleetVehicle
        fields = '__all__'


