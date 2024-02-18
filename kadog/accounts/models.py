from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields

    class Sex(models.TextChoices):
        MALE = 'Male', 'male'
        FEMALE = 'Female', 'female'
        OTHER = 'Other', 'other'

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10,choices=Sex.choices,default=Sex.MALE, null=True,blank=True)

    def __str__(self):
        return self.username