from django.db import models

from core.models import UserTimestampMixin
from .enums import VehicleTypeEnum
from .enums import ColorEnum
from people.models import Customer


class Make(UserTimestampMixin):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Makes'

    def __str__(self):
        return self.name


class Model(UserTimestampMixin):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    vehicle_type = models.IntegerField(choices=VehicleTypeEnum.choices)

    class Meta:
        verbose_name_plural = 'Models'
        unique_together = ('make', 'name')

    def __str__(self):
        return f'{self.make.name} {self.name}'


class Vehicle(UserTimestampMixin):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=10)
    vin = models.CharField(max_length=17, blank=True, null=True)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.IntegerField()
    last_reading_mileage = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(choices=ColorEnum.choices)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=True)
    is_primary = models.BooleanField(default=True)
    is_secondary = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Vehicles'
