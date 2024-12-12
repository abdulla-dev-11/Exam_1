from django.urls import path

from .views import VehiclesDetail, VehiclesViewSet, SensorsDetail, SensorsViewSet, ServiceCentersDetail, \
    ServiceCentersViewSet, MaintenanceDetail, MaintenanceViewSet

urlpatterns = [
    path('vehicles/', VehiclesViewSet.as_view()),
    path('vehicles/<int:pk>/', VehiclesDetail.as_view()),
    path('sensors/', SensorsViewSet.as_view()),
    path('sensors/<int:pk>/', SensorsDetail.as_view()),
    path('maintenance/', MaintenanceViewSet.as_view()),
    path('maintenance/<int:pk>/', MaintenanceDetail.as_view()),
    path('servicecenters/', ServiceCentersViewSet.as_view()),
    path('servicecenters/<int:pk>/', ServiceCentersDetail.as_view()),

]
