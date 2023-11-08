from django.db import models
from django.utils.translation import gettext_lazy as _


class PersonTypeEnum(models.IntegerChoices):
    EMPLOYEE = 1, _('Employee')
    CUSTOMER = 2, _('Customer')
    VENDOR = 3, _('Vendor')
    OTHER = 4, _('Other')
