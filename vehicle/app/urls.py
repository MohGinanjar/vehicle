from django.urls import path
from .views import * 


urlpatterns = [
    path('api2/public/workplan/viewVehicleDriver', ListFleetVehicle.as_view(), name="list-vehicle"),
    path('api2/public/workplan/deleteVehicleDriver', FleetVehicleDelete.as_view(), name="delete-vehicle"),
]