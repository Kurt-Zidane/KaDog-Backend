# events/serializers.py
from rest_framework import serializers
from .models import PetEntertainment

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        allow_null=True
    )    
    class Meta:
        model = PetEntertainment
        fields = '__all__'

