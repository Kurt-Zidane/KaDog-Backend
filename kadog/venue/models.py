from django.db import models

# Create your models here.

class Venue(models.Model):
    venue_place = models.CharField(max_length=100)
    venue_date = models.DateField(null=True)
    description = models.TextField(default='Please input the information for this event.')
    events = models.ManyToManyField('events.Event')

    def __str__(self):
        return self.venue_place
