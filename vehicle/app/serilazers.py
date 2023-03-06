from .models import FleetVehicle
from rest_framework import serializers



class FleetVehicleSerializers(serializers.ModelSerializer):
    class Meta :
        model = FleetVehicle
        fields = '__all__'


