from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import DogSerializer
from .models import Dog
class DogViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        queryset = Dog.objects.all().order_by('date_created')
        return queryset