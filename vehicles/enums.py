from django.db import models
from django.utils.translation import gettext_lazy as _


class VehicleTypeEnum(models.IntegerChoices):
    CAR = 1, _('Car')
    MOTORBIKE = 2, _('Motorbike')
    TRUCK = 3, _('Truck')
    VAN = 4, _('Van')
    BUS = 5, _('Bus')
    MOTORCYCLE = 6, _('Motorcycle')
    TRAILER = 7, _('Trailer')
    MISC = 8, _('Miscellaneous')
