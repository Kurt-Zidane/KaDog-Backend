from django.db import models
from django.utils.timezone import now
from accounts.models import CustomUser

class Event(models.Model):
          
    title = models.CharField(max_length=100)
    date_field = models.DateField(null=True)
    description = models.TextField(default='Please input the information for this event.')
    participants = models.ManyToManyField(CustomUser, through='EventUserParticipant')

    # Add more fields as needed
    
    def __str__(self):
        return self.title
    
from accounts.models import CustomUser

class EventUserParticipant(models.Model):
    participant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=now, editable=False)

    class Meta:
        # Unique constraint to ensure each user is associated with an event only once
        unique_together = ('participant', 'event')
    
    def __str__(self):
        # Format the datetime as a string using strftime
        return f"{self.participant.username} - {self.event} - {self.date_joined.strftime('%Y-%m-%d %H:%M:%S')}"