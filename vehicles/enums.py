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


class ColorEnum(models.IntegerChoices):
    BLACK = 1, _('Black')
    WHITE = 2, _('White')
    RED = 3, _('Red')
    GREEN = 4, _('Green')
    BLUE = 5, _('Blue')
    YELLOW = 6, _('Yellow')
    ORANGE = 7, _('Orange')
    PURPLE = 8, _('Purple')
    GRAY = 9, _('Gray')
    BROWN = 10, _('Brown')
    PINK = 11, _('Pink')
    GOLD = 12, _('Gold')
    SILVER = 13, _('Silver')
    CYAN = 14, _('Cyan')
    MAGENTA = 15, _('Magenta')
    LIME = 16, _('Lime')
    MAROON = 17, _('Maroon')
    NAVY = 18, _('Navy')
    OLIVE = 19, _('Olive')
    TEAL = 20, _('Teal')
    VIOLET = 21, _('Violet')
    ROSE = 22, _('Rose')
    CRIMSON = 23, _('Crimson')
    TAN = 24, _('Tan')
    TURQUOISE = 25, _('Turquoise')
