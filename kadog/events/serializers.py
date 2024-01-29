# events/serializers.py
from rest_framework import serializers
from .models import Event
from .models import EventUserParticipant

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUserParticipant
        fields = ['id','participant', 'event', 'date_joined']
