from django.db import models
from django.utils.translation import gettext_lazy as _


class VehicleTypeEnum(models.IntegerChoices):
    CAR = 1, _('Car')
    SUV = 2, _('SUV')
    PICKUP = 3, _('Pickup')
    TRUCK = 4, _('Truck')
    VAN = 5, _('Van')
    BUS = 6, _('Bus')
    MOTORCYCLE = 7, _('Motorcycle')
    TRAILER = 8, _('Trailer')
