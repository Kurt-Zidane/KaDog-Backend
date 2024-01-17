from django.db import models

class Vaccine(models.Model):
          
    vaccination_title = models.CharField(max_length=100)
    vaccination_type = models.CharField(max_length=100)
    vaccination_date = models.DateField(null=True)
    description = models.TextField(default='Please input the information for this vaccine.')
    # Add more fields as needed
    
    def __str__(self):
        return self.title