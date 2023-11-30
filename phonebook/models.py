from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contact(models.Model):
    DEPARTMENT_CHOICES = [
        ('it', 'IT'),
        ('isoc', 'ISOC'),
    ]

    name = models.CharField(max_length=50)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, default="employee")
    email = models.EmailField()
    phone_number = PhoneNumberField(null=True, blank=True)
    mobile_number = PhoneNumberField(null=True, blank=True)
    room_location = models.CharField(max_length=100, null=True, blank=True)
    #If employee is actively employed than True.
    active_employee = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

