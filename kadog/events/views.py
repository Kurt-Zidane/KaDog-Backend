from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event

class EventViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer