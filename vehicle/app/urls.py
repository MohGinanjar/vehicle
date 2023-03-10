from django.urls import path
from .views import * 


urlpatterns = [
    path('api2/public/workplan/viewVehicleDriver', ListFleetVehicle.as_view(), name="list-vehicle"),
    path('api2/public/workplan/deleteVehicleDriver', FleetVehicleDelete.as_view(), name="delete-vehicle"),
    path('api2/public/workplan/viewVehicleCategory', ListFleetVehicleCategory.as_view(), name="category-vehicle"),
    path('api2/public/workplan/setVehicleCategory', FleetVehicleCreateView.as_view(), name="create-vehicle"),
]