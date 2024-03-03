from django.contrib import admin
from .models import Venue, DogEvent,VenueEventsParticipant
# Register your models here.

admin.site.register(Venue)
admin.site.register(DogEvent)
admin.site.register(VenueEventsParticipant)