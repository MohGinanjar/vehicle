from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(FleetVehicle)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass


@admin.register(FleetVehicleModelBrand)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass

@admin.register(FleetVehicleModelCategory)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass

@admin.register(TrxFleetDriver)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass

@admin.register(HrEmployee)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass

@admin.register(TrxFleetWorkingVehicleDriver)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass

@admin.register(FleetVehicleModel)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass


@admin.register(FleetVehicleOdometer)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass

@admin.register(FleetVehicleTag)
class MasterCompanyAdmin( admin.ModelAdmin):
    pass
