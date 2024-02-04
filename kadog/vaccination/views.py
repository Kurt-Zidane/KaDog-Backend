from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import VaccineSerializer
from .serializers import VaccineUserRelationshipSerializer
from .models import Vaccine
from .models import VaccineUserParticipant

class VaccineListView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

class VaccineUserRelationshipCreateView(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = VaccineUserParticipant.objects.all()
    serializer_class = VaccineUserRelationshipSerializer