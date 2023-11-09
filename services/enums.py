from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethodEnum(models.IntegerChoices):
    CASH = 1, _('Cash')
    CREDIT_CARD = 2, _('Credit Card')
    DEBIT_CARD = 3, _('Debit Card')
    BANK_TRANSFER = 4, _('Bank Transfer')
    PAYPAL = 5, _('Paypal')
    OTHER = 6, _('Other')
