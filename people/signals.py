from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver

from .enums import PersonTypeEnum
from .models import Customer
from .models import Employee


@receiver(post_save, sender=Employee)
def update_employee_person_type(sender, instance, created, **kwargs):
    if created:
        instance.person_type = PersonTypeEnum.EMPLOYEE
        instance.save()


EmployeeModel = apps.get_model('people', 'Employee')
post_save.connect(update_employee_person_type, sender=EmployeeModel)


@receiver(post_save, sender=Customer)
def update_customer_person_type(sender, instance, created, **kwargs):
    if created:
        instance.person_type = PersonTypeEnum.CUSTOMER
        instance.save()


CustomerModel = apps.get_model('people', 'Customer')
post_save.connect(update_customer_person_type, sender=CustomerModel)
