# events/serializers.py
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        allow_null=True
    )    
    class Meta:
        model = Event
        fields = '__all__'

