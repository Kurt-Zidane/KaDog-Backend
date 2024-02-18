from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    SEX_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    sex = serializers.ChoiceField(choices=SEX_CHOICES)
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = [
                    'username', 
                    'email', 
                    'first_name', 
                    'last_name', 
                    'sex',
                    'password',
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
            sex=self.validated_data['sex'],
            password=self.validated_data['password'],

        )
        user.is_active = True
        user.save()

        return user

class CustomUserCurrentSerializer(UserSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name','sex')