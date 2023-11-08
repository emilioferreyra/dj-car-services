from django.db import models

from core.models import UserTimestampMixin
from .enums import PersonTypeEnum


class Person(UserTimestampMixin):
    person_type = models.IntegerField(choices=PersonTypeEnum.choices)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'People'


class Employee(Person):
    birth_date = models.DateField()
    doc_id = models.CharField(max_length=30)
    salary = models.DecimalField(decimal_places=2, max_digits=22)

    class Meta:
        verbose_name_plural = 'Employees'
