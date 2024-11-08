from .models import PetName
from rest_framework import serializers
from accounts.models import CustomUser

class DogSerializer(serializers.ModelSerializer):
    owner_token = serializers.CharField(write_only=True)
    date_created = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)
    
    class Meta:
        model = PetName
        fields = ('id', 'name', 'breed', 'dog_gender', 'dog_size', 'dog_age', 'owner_token', 'date_created')
        read_only_fields = ('id', 'date_created')

    def create(self, validated_data):
        owner_token = validated_data.pop('owner_token')
        owner = CustomUser.objects.get(auth_token=owner_token)  # Assuming you have an auth_token field in CustomUser model
        dog = PetName.objects.create(owner=owner, **validated_data)
        return dog


