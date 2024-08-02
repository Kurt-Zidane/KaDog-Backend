from rest_framework import serializers
from .models import Vaccine
from .models import VaccineUserParticipant
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer
from dogs.models import PetName

class DogSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = PetName
        fields = ('id', 'name', 'breed','dog_size','dog_age','owner')  # Adjust fields as needed

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
    owner_token = serializers.CharField(write_only=True)
    class Meta:
        model = VaccineUserParticipant
        fields = ('id','attendee','vaccine','dog','owner_token','date_joined')
        read_only_fields = ('id','date_joined')
        
    def create(self, validated_data):
        owner_token = validated_data.pop('owner_token')
        owner = CustomUser.objects.get(auth_token=owner_token)  # Assuming you have an auth_token field in CustomUser model
        vaccine = VaccineUserParticipant.objects.create(owner=owner, **validated_data)
        return vaccine
    
class DogVaccineListSerializer(serializers.ModelSerializer):
    dog = DogSerializer()
    
    class Meta:
        model = VaccineUserParticipant
        fields = ('id','attendee','vaccine','dog','date_joined')
        read_only_fields = ('id','date_joined')