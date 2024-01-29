from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import EventSerializer
from .serializers import EventUserRelationshipSerializer
from .models import Event
from .models import EventUserParticipant

class EventViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUserRelationshipCreateView(generics.CreateAPIView):
    queryset = EventUserParticipant.objects.all()
    serializer_class = EventUserRelationshipSerializer