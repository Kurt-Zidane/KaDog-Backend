from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    dogs = serializers.PrimaryKeyRelatedField(
        many=True, allow_null=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
                    'username', 
                    'email', 
                    'first_name', 
                    'last_name', 
                    'password',
                    'dogs'
                ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = CustomUser.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            password=self.validated_data['password'],

        )
        user.is_active = False
        user.save()

        return user
