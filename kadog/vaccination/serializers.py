from rest_framework import serializers
from .models import Vaccine
from .models import VaccineUserParticipant

class VaccineSerializer(serializers.ModelSerializer):
    participants = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Vaccine
        fields = '__all__'

class VaccineUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineUserParticipant
        fields = '__all__'