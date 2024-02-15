from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from .serializers import EventUserRelationshipSerializer
from .models import Event
from .models import EventUserParticipant

from accounts.models import CustomUser


class EventListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUserRelationshipCreateView(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = EventUserParticipant.objects.all()
    serializer_class = EventUserRelationshipSerializer

class ParticipantListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]  # Add permissions if needed
    queryset = Event.objects.prefetch_related('participants')
    serializer_class = EventSerializer