from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from .serializers import EventUserRelationshipSerializer
from .models import Event
from .models import EventUserParticipant

class EventListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUserRelationshipCreateView(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = EventUserParticipant.objects.all()
    serializer_class = EventUserRelationshipSerializer