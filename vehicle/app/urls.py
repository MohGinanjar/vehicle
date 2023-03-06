from django.urls import path
from .views import * 


urlpatterns = [
    path('list-vehicle/', ListFleetVehicle.as_view(), name="list-vehicle"),
]