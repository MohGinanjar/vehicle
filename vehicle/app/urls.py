from django.urls import path
from .views import * 


urlpatterns = [
    path('api2/public/workplan/viewVehicleDriver', ListFleetVehicle.as_view(), name="list-vehicle"),
    # path('api2/public/workplan/deleteVehicleDriver', FleetVehicleDelete.as_view(), name="delete-vehicle"),
    # path('api2/public/workplan/viewVehicleCategory', ListFleetVehicleCategory.as_view(), name="category-vehicle"),
    # path('api2/public/workplan/setVehicleCategory', FleetVehicleCreateView.as_view(), name="create-vehicle"),
    # path('api2/public/workplan/viewRotation', ListVehicleRotation.as_view(), name="rotation-vehicle"),
    # path('api2/public/workplan/setRotation', RotationVehicleCreateView.as_view(), name="create-rotation-vehicle"),
    # path('api2/public/workplan/deleteRotation', RotationVehicleDelete.as_view(), name="delete-rotation-vehicle"),
    # path('api2/public/workplan/clockIn', TimeSheetCreateView.as_view(), name="timesheet"),
]