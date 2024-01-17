from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import VaccineSerializer
from .models import Vaccine

class VaccineViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer