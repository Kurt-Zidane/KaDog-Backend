from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_judge = models.BooleanField(default=False)

    class Sex(models.TextChoices):
        MALE = 'Male', 'male'
        FEMALE = 'Female', 'female'
        OTHER = 'Other', 'other'

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10,choices=Sex.choices,default=Sex.MALE, null=True,blank=True)
    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username