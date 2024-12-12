from rest_framework import serializers

from .models import Vehicles, Sensors, Maintenance, ServiceCenters


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('id', 'model', 'year', 'vin')


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ['id', 'type', 'installed_date', 'vehicle']


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['id', 'service_type', 'service_date', 'vehicle']


class ServiceCentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenters
        fields = ['id', 'name', 'address', 'rating']
