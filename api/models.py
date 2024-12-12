from django.db import models


class Vehicles(models.Model):
    model = models.CharField(max_length=100)
    year = models.DateField()
    vin = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return self.model


class Sensors(models.Model):
    type = models.CharField(max_length=255)
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    installed_date = models.DateField()


    def __str__(self):
        return self.type


class Maintenance(models.Model):
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=255)
    scheduled_date = models.DateField()

    def __str__(self):
        return self.service_type


class ServiceCenters(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating = models.FloatField(max_length=3)

    def __str__(self):
        return self.name