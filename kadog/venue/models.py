from django.db import models
from django.utils.timezone import now
from accounts.models import CustomUser
from events.models import Event
from dogs.models import PetName
# Create your models here.

class Venue(models.Model):
    venue_place = models.CharField(max_length=100)
    venue_date = models.DateField(null=True)
    description = models.TextField(default='Please input the information for this event.')
    events = models.ManyToManyField('events.Event', through='VenueEventsParticipant')

    def __str__(self):
        return self.venue_place
    
class VenueEventsParticipant(models.Model):
    venue = models.ForeignKey('venue.Venue', on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.event.title
    
    class Meta:
        # Unique constraint to ensure each user is associated with an event only once
        unique_together = ('venue', 'event')

class DogEvent(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    dog = models.ForeignKey('dogs.PetName', on_delete=models.CASCADE)
    attendee = models.CharField(max_length=50,blank=True)
    date_joined = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.event.title} - {self.dog.name}"
    
    class Meta:
        # Unique constraint to ensure each user is associated with an event only once
        unique_together = ('dog', 'event')

