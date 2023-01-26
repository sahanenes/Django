from django.db import models

GEAR = (
        ("Auto", "Automatic"),
        ("Manual", "Manual"),)

class Car(models.Model):
    plate_number = models.CharField(max_length=15,unique=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=6,choices=GEAR)
    rent_per_day = models.SmallIntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand}/{self.model}-{self.plate_number}"