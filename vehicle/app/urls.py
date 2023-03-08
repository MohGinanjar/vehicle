from django.urls import path
from .views import * 


urlpatterns = [
    path('api2/public/workplan/viewVehicleDriver', ListFleetVehicle.as_view(), name="list-vehicle"),
]