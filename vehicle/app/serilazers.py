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
        


# class VehicleCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FleetVehicleModelCategory
#         fields = '__all__'

# class FleetVehicleSerializers(serializers.ModelSerializer):
#     vehicleID = serializers.ReadOnlyField(source='id')
#     vehicleCategoryID = serializers.ReadOnlyField(source='vehicle_category.id')
#     employeeID = serializers.ReadOnlyField(source='driver.id')
#     driverID = serializers.ReadOnlyField(source='driver.id')
#     employeeName = serializers.ReadOnlyField(source='driver.employee_name')
#     date = serializers.ReadOnlyField(source='driver.date_join')
#     category_name = serializers.ReadOnlyField(source='vehicle_category.category_name')
#     model_year = serializers.ReadOnlyField(source='vehicle_brand.model_year')
#     fuel_type = serializers.ReadOnlyField(source='vehicle_brand.brand.fuel_type')
#     brand_name = serializers.ReadOnlyField(source='vehicle_brand.brand.brand_name')
#     vehicle_brand = serializers.ReadOnlyField(source='vehicle_brand.brand.brand_name')
#     vehicle_type = serializers.ReadOnlyField(source='vehicle_brand.brand.vehicle_type.vehicle_type')
#     model_name = serializers.ReadOnlyField(source='vehicle_brand.vehicle_type')
#     # #drivers = DriverSerializer(many=False, read_only=True)
    
#     class Meta :
#         model = FleetVehicle
#         fields = '__all__'
    
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         odo = FleetVehicleOdometer.objects.filter(id=data['odomoter']).values('value', 'created_date')
#         data['vehicleDescription'] = {
#             'category_id':data['vehicle_category'],
#             'category_name':data['model_name'],
#             'license_plate':data['license_plate'],
#             'vin_sn':data['vin_sn'],
#             'active':data['active'],
#             'location':data['location'],
#             'brand_name':data['brand_name'],
#             'model_year':data['model_year'],
#             'fuel_type':data['fuel_type'],
#             'vehicle_type':data['vehicle_type'],
#             'odometer':odo
#         }
#         del data['license_plate']
#         del data['vin_sn']
#         del data['active']
#         del data['location']
#         del data['brand_name']
#         del data['model_year']
#         del data['fuel_type']
#         del data['vehicle_type']
#         del data['odomoter']
#         del data['driver']
#         del data['id']
#         return data
        #         try:
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
        
        

# class VehicleRotationSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = VehicleRotation
#         fields = ['value_rotation']
        
#     def to_representation(self, instance):
#         return instance.value_rotation

        
# class RotationSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = VehicleRotation
#         fields = '__all__'
        

# class TimeSheetSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = TimeSheet
#         fields = '__all__'
        


# class FleetVehicleSerializers(serializers.ModelSerializer):
#     # vehicleID = serializers.ReadOnlyField(source='id')
#     # vehicleCategoryID = serializers.ReadOnlyField(source='vehicle_category.id')
#     # employeeID = serializers.ReadOnlyField(source='driver.id')
#     # driverID = serializers.ReadOnlyField(source='driver.id')
#     # employeeName = serializers.ReadOnlyField(source='driver.employee_name')
#     # date = serializers.ReadOnlyField(source='driver.date_join')
#     # category_name = serializers.ReadOnlyField(source='vehicle_category.category_name')
#     # model_year = serializers.ReadOnlyField(source='vehicle_brand.model_year')
#     # fuel_type = serializers.ReadOnlyField(source='vehicle_brand.brand.fuel_type')
#     # brand_name = serializers.ReadOnlyField(source='vehicle_brand.brand.brand_name')
#     # vehicle_brand = serializers.ReadOnlyField(source='vehicle_brand.brand.brand_name')
#     # vehicle_type = serializers.ReadOnlyField(source='vehicle_brand.brand.vehicle_type.vehicle_type')
#     # model_name = serializers.ReadOnlyField(source='vehicle_brand.vehicle_type')
#     # #drivers = DriverSerializer(many=False, read_only=True)
#     vehicle_rotation = VehicleRotationSerializers(many=True, read_only=True)
    
#     class Meta :
#         model = FleetVehicle
#         fields = '__all__'


