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
    sex = serializers.ChoiceField(choices=SEX_CHOICES, allow_blank=True, required=False)
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    contact_number = serializers.CharField(allow_blank=True, required=False)
    
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'sex',
            'password',
            'contact_number'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        # Get the value of 'sex' from the validated data, defaulting to an empty string if not present
        sex = self.validated_data.get('sex', '')
        contact_number = self.validated_data.get('contact_number','')
        
        # Create the user using the retrieved or default value for 'sex'
        user = CustomUser.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            sex=sex,  # Use the retrieved or default value for 'sex'
            contact_number=contact_number,
            password=self.validated_data['password'],
        )
        user.is_active = True
        user.save()

        return user

class CustomUserCurrentSerializer(UserSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta(UserSerializer.Meta):
        fields = ('id', 'first_name', 'last_name','sex','contact_number','email')
        read_only_fields = ['id','email']
