# views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DogSerializer
from .models import PetName

class DogListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PetName.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        # Make a mutable copy of the request data
        mutable_data = request.data.copy()
        
        # Extract token from Authorization header
        auth_token = request.headers.get('Authorization').split(' ')[1]
        mutable_data['owner_token'] = auth_token

        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)