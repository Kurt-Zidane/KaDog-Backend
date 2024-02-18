from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from .models import Event

class EventListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
