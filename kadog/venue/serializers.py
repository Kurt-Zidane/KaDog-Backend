# venue/serializers.py
from rest_framework import serializers
from .models import Venue,VenueEventsParticipant, DogEvent
from dogs.models import Dog
from accounts.serializers import CustomUserSerializer
from events.models import Event

class DogSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed','dog_size','dog_age','owner')  # Adjust fields as needed

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description')  # Adjust fields as needed

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class VenueEventSerializer(serializers.ModelSerializer):
    venue = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='venue_place'
    )
    event = EventSerializer()
    class Meta:
        model = VenueEventsParticipant
        fields = '__all__'

class DogEventListSerializer(serializers.ModelSerializer):
    dog = DogSerializer()

    class Meta:
        model = DogEvent
        fields = '__all__'

class DogEventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogEvent
        fields = '__all__'

