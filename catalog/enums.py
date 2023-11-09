from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryEnum(models.IntegerChoices):
    PRODUCT = 1, _('Product')
    SERVICE = 2, _('Service')
    OTHER = 3, _('Other')
