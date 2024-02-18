from django.db import models
from django.utils.timezone import now
from accounts.models import CustomUser

class Event(models.Model):
          
    title = models.CharField(max_length=100)
    description = models.TextField(default='Please input the information for this event.')
    venues = models.ManyToManyField('venue.Venue', through='venue.VenueEventsParticipants')
    # Add more fields as needed
    
    def __str__(self):
        return self.title
    