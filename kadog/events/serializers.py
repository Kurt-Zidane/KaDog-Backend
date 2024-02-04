# events/serializers.py
from rest_framework import serializers
from .models import Event
from .models import EventUserParticipant

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )    
    class Meta:
        model = Event
        fields = '__all__'

class EventUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUserParticipant
        fields = ['id','participant', 'event', 'date_joined']
