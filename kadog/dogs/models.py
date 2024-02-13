from django.db import models
from django.utils.timezone import now
from accounts.models import CustomUser

class Dog(models.Model):
    class DogSize(models.TextChoices):
        SMALL = 'Small', 'small'
        MEDIUM = 'Medium', 'medium'
        LARGE = 'Large', 'large'
        EXTRA_LARGE = 'Extra large', 'extra large'

    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    dog_size = models.CharField(max_length=15, choices=DogSize.choices, default=DogSize.SMALL)
    date_created = models.DateTimeField(default=now, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Add more fields as needed
    class Meta:
        # Unique constraint to ensure each user is associated with an event only once
        unique_together = ('owner', 'name')
    
    def __str__(self):
        # Format the datetime as a string using strftime
        return f"Owner: {self.owner.username} | Dog Name: {self.name} | Dog Breed: {self.breed}"
    
