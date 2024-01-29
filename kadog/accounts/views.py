# accounts/views.py or accounts/api/views.py
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer