from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import VenueSerializer
from .models import Venue

class VenueListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetailView(generics.RetrieveAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

