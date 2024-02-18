from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import DogSerializer
from .models import Dog

class DogListAPIView(generics.ListAPIView):
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        # Filter the queryset based on the authenticated user
        user = self.request.user
        if user.is_authenticated:
            return Dog.objects.filter(owner=user)
        else:
            return Dog.objects.none()  # Return an empty queryset if the user is not authenticated
