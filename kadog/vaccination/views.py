from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializers import VaccineSerializer
from .serializers import VaccineUserRelationshipSerializer
from .models import Vaccine
from .models import VaccineUserParticipant

class VaccineViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

class VaccineUserRelationshipCreateView(generics.CreateAPIView):
    queryset = VaccineUserParticipant.objects.all()
    serializer_class = VaccineUserRelationshipSerializer