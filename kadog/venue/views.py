from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import VenueSerializer, VenueEventSerializer, DogEventListSerializer, DogEventCreateSerializer
from .models import Venue, VenueEventsParticipant, DogEvent
from rest_framework.response import Response
from rest_framework.views import APIView

class VenueListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetailView(generics.RetrieveAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueEventListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = VenueEventsParticipant.objects.all()
    serializer_class = VenueEventSerializer

class DogEventCreateView(generics.CreateAPIView):
    queryset = DogEvent.objects.all()
    serializer_class = DogEventCreateSerializer

class DogEventListView(generics.ListAPIView):
    serializer_class = DogEventListSerializer

    def get_queryset(self):
        # Get the event_id from the URL parameter
        event_id = self.kwargs['event_id']
        
        # Filter DogEvent queryset based on the event_id
        queryset = DogEvent.objects.filter(event_id=event_id)
        
        return queryset


class DogEventTotalView(APIView):

    def get(self, request, format=None):
        total_dogs = DogEvent.objects.count()
        return Response({"total_dogs": total_dogs})