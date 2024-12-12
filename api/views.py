from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Vehicles, Sensors, ServiceCenters, Maintenance
from .serializers import VehiclesSerializer, SensorsSerializer, ServiceCentersSerializer, MaintenanceSerializer


class VehiclesViewSet(ListCreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer


class VehiclesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer


class SensorsViewSet(ListCreateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class SensorsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class MaintenanceViewSet(ListCreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class MaintenanceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ServiceCentersViewSet(ListCreateAPIView):
    queryset = ServiceCenters.objects.all()
    serializer_class = ServiceCentersSerializer


class ServiceCentersDetail(RetrieveUpdateDestroyAPIView):
    queryset = ServiceCenters.objects.all()
    serializer_class = ServiceCentersSerializer
