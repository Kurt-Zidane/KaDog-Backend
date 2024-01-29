from django.contrib import admin
from .models import Event
from .models import EventUserParticipant
# Register your models here.

admin.site.register(Event)
admin.site.register(EventUserParticipant)