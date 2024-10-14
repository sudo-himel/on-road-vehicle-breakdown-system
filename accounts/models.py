from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class CustomUser(AbstractBaseUser):
    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Bike', 'Bike')
    ]
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES, blank=True, null=True)
    model_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_of_employees = models.PositiveIntegerField(blank=True, null=True)
    is_garage = models.BooleanField(default=False)
