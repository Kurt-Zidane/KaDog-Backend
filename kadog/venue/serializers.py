# events/serializers.py
from rest_framework import serializers
from .models import Venue

class VenueSerializer(serializers.ModelSerializer):
    events = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field= 'title'
    )    
    class Meta:
        model = Venue
        fields = '__all__'
