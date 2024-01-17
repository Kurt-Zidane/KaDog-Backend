from rest_framework import serializers
from .models import Vaccine

class VaccineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'
