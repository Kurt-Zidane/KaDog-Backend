from django.contrib import admin
from .models import Vaccine
from .models import VaccineUserParticipant
# Register your models here.

admin.site.register(Vaccine)
admin.site.register(VaccineUserParticipant)