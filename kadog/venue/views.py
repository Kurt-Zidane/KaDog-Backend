from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import VenueSerializer, VenueEventSerializer, DogEventListSerializer, DogEventCreateSerializer
from .models import Venue, VenueEventsParticipants, DogEvent
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
    queryset = VenueEventsParticipants.objects.all()
    serializer_class = VenueEventSerializer

class DogEventCreateView(generics.CreateAPIView):
    queryset = DogEvent.objects.all()
    serializer_class = DogEventCreateSerializer

class DogEventListView(generics.ListAPIView):
    queryset = DogEvent.objects.all()
    serializer_class = DogEventListSerializer

class DogEventTotalView(APIView):

    def get(self, request, format=None):
        total_dogs = DogEvent.objects.count()
        return Response({"total_dogs": total_dogs})