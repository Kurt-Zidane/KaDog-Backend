from django.contrib import admin
from .models import Venue, DogEvent,VenueEventsParticipants
# Register your models here.

admin.site.register(Venue)
admin.site.register(DogEvent)
admin.site.register(VenueEventsParticipants)