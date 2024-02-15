from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djoser.views import UserViewSet
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserCurrentSerializer
from rest_framework.views import APIView

class CustomUserCurrentViewSet(UserViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # Override the `get_serializer_class` method to return the appropriate serializer
    def get_serializer_class(self):
        if self.action == 'retrieve':
            # For listing or retrieving, return serializer with additional fields
            return CustomUserSerializer
        else:
            # For other actions, use the default serializer
            return super().get_serializer_class()
        
class CustomUserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class TotalUserCountView(APIView):
    def get(self, request, *args, **kwargs):
        total_users = CustomUser.objects.count()
        return Response({"total_users": total_users})