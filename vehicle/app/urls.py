from django.urls import path
from .views import * 


urlpatterns = [
    path('api2/public/workplan/viewVehicleDriver', ListFleetVehicle.as_view(), name="list-vehicle"),
    path('api2/public/workplan/setVehicleDriver', TrxFleetWorkingVehicleDriverView.as_view(), name="set-vehicle"),
    path('api2/public/workplan/deleteVehicleDriver', deleteVehicleDriver.as_view(), name="delete-vehicle"),
    path('api2/public/workplan/setRotation', viewRotation.as_view(), name="set-rotation"),
    # path('api2/public/workplan/setVehicleCategory', FleetVehicleCreateView.as_view(), name="create-vehicle"),
    # path('api2/public/workplan/viewRotation', ListVehicleRotation.as_view(), name="rotation-vehicle"),
    # path('api2/public/workplan/setRotation', RotationVehicleCreateView.as_view(), name="create-rotation-vehicle"),
    # path('api2/public/workplan/deleteRotation', RotationVehicleDelete.as_view(), name="delete-rotation-vehicle"),
    # path('api2/public/workplan/clockIn', TimeSheetCreateView.as_view(), name="timesheet"),
]