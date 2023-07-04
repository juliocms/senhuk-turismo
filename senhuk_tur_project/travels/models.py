from django.db import models

class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    responsible_guide = models.TextField(max_length=60, null=False)
    departure_destination = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=255, null=False)
    type = models.TextField(max_length=30, null=False)
    vehicle_plate = models.TextField(max_length=10, null=False)
    date_departure = models.DateField(null=True, blank=True)
    date_arrival = models.DateField(null=True, blank=True)
 
    def __str__(self):
        return f"{self.departure_destination} | {self.date_arrival} - {self.date_departure}"
