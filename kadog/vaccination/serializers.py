from rest_framework import serializers
from .models import Vaccine
from .models import VaccineUserParticipant
class VaccineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'

class VaccineUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineUserParticipant
        fields = ['id','vaccine', 'participant', 'date_joined']