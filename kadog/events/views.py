from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from .models import PetEntertainment

class EventListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = PetEntertainment.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveAPIView):
    queryset = PetEntertainment.objects.all()
    serializer_class = EventSerializer
