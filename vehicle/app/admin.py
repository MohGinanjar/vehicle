from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(FleetVehicle)
class MasterCompanyAdmin(admin.ModelAdmin):
    pass


# @admin.register(VehicleBrand)
# class MasterCompanyAdmin( admin.ModelAdmin):
#     pass

# @admin.register(FleetVehicleModelCategory)
# class MasterCompanyAdmin( admin.ModelAdmin):
#     pass

# @admin.register(VehicleType)
# class MasterCompanyAdmin( admin.ModelAdmin):
#     pass

# @admin.register(FleetVehicleOdometer)
# class MasterCompanyAdmin( admin.ModelAdmin):
#     pass

# @admin.register(VehicleEmployee)
# class MasterCompanyAdmin( admin.ModelAdmin):
#     pass

# @admin.register(FleetVehicleModel)
# class MasterCompanyAdmin( admin.ModelAdmin):
#     pass

# @admin.register(VehicleRotation)
# class MasterCompanyAdmin( admin.ModelAdmin):
#     pass