# events/serializers.py
from rest_framework import serializers
from .models import Event
from .models import EventUserParticipant

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        allow_null=True
    )    
    class Meta:
        model = Event
        fields = '__all__'

class EventUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUserParticipant
        fields = '__all__'
