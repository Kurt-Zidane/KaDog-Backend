from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from .serializers import VaccineSerializer
from .serializers import VaccineUserRelationshipSerializer
from .serializers import DogVaccineListSerializer
from .models import Vaccine
from .models import VaccineUserParticipant
from rest_framework.response import Response

class VaccineListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

class VaccineUserRelationshipCreateView(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    # queryset = VaccineUserParticipant.objects.all()
    serializer_class = VaccineUserRelationshipSerializer
    
    def get_queryset(self):
        return Vaccine.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        # Make a mutable copy of the request data
        mutable_data = request.data.copy()
        
        # Extract token from Authorization header
        auth_header = request.headers.get('Authorization')
        if auth_header is not None:
            auth_token = auth_header.split(' ')[1]
            mutable_data['owner_token'] = auth_token
        else:
            # Handle the case where the Authorization header is missing
            return Response({"error": "Authorization header is missing"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DogVaccineListView(generics.ListAPIView):
    serializer_class = DogVaccineListSerializer

    def get_queryset(self):
        # Get the event_id from the URL parameter
        vaccine_id = self.kwargs['vaccine_id']
        
        # Filter DogEvent queryset based on the event_id
        queryset = VaccineUserParticipant.objects.filter(vaccine_id=vaccine_id)
        
        return queryset