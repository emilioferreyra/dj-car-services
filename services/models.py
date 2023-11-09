from django.db import models

from core.models import UserTimestampMixin
from people.models import Customer
from people.models import Employee
from catalog.models import Catalog
from vehicles.models import Vehicle
from .enums import PaymentMethodEnum


class Order(UserTimestampMixin):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    payment_method = models.IntegerField(choices=PaymentMethodEnum.choices)
    payment_status = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.customer} {self.vehicle}'


class OrderItem(UserTimestampMixin):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f'{self.order} {self.catalog}'