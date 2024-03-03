from django.db import models
from django.utils.timezone import now
from accounts.models import CustomUser

class Vaccine(models.Model):
          
    vaccination_title = models.CharField(max_length=100)
    vaccination_type = models.CharField(max_length=100)
    vaccination_date = models.DateField(null=True)
    description = models.TextField(default='Please input the information for this vaccine.')
    participants = models.ManyToManyField(CustomUser, through='VaccineUserParticipant')
    # Add more fields as needed
    
    def __str__(self):
        return self.vaccination_title
    
class VaccineUserParticipant(models.Model):
    attendee = models.CharField(max_length=50,blank=True)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dog = models.ForeignKey('dogs.Dog', on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=now, editable=False)
    # Add more fields as needed

    class Meta:
        # Unique constraint to ensure each user is associated with an event only once
        unique_together = ('owner', 'vaccine')
    
    def __str__(self):
        # Format the datetime as a string using strftime
        return f"{self.owner.username} - {self.vaccine} - {self.date_joined.strftime('%Y-%m-%d %H:%M:%S')}"