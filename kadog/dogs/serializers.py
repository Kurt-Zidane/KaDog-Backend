from .models import Dog
from rest_framework import serializers
from accounts.models import CustomUser

class DogSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    date_created = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)
    
    class Meta:
        model = Dog
        fields = ('id','name','breed','dog_gender','dog_size','owner','date_created')
        read_only_fields =('id','date_created')
