# views.py
from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication# Import TokenAuthentication
from .serializers import DogSerializer
from .models import PetName

class DogListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetName.objects.all()
    serializer_class = DogSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PetName.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        # Make a mutable copy of the request data
        mutable_data = request.data.copy()
        
        # Extract token from Authorization header
        auth_token = request.headers.get('Authorization').split(' ')[1]
        mutable_data['owner_token'] = auth_token

        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetailView(generics.RetrieveAPIView):
    queryset = PetName.objects.all()
    serializer_class = DogSerializer
    lookup_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dog_id = self.kwargs['pk']
        context['selected_dog'] = DogSerializer(PetName.objects.get(pk=dog_id)).data
        return context  
    
class DogUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = PetName.objects.all()
    serializer_class = DogSerializer
    #permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        try:
            dog = self.get_object()
        except PetName.DoesNotExist:
            return Response({'error': 'Dog not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        dog.name = data.get('name') or dog.name
        dog.breed = data.get('breed') or dog.breed
        dog.dog_gender = data.get('dog_gender') or dog.dog_gender
        dog.dog_size = data.get('dog_size') or dog.dog_size
        dog.dog_age = data.get('dog_age') or dog.dog_age
        
        dog.save()
    
        return Response(DogSerializer(dog).data, status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        try:
            dog = self.get_object()
        except PetName.DoesNotExist:
            return Response({'error': 'Dog not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update dog fields based on request data
        dog.name = request.data.get('name', dog.name)
        dog.breed = request.data.get('breed', dog.breed)
        dog.dog_gender = request.data.get('dog_gender', dog.dog_gender)
        dog.dog_size = request.data.get('dog_size', dog.dog_size)
        dog.dog_age = request.data.get('dog_age', dog.dog_age)
        
        dog.save()
        
        return Response(DogSerializer(dog).data, status=status.HTTP_200_OK)


class DogRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = PetName.objects.all()
    serializer_class = DogSerializer
    #authentication_classes = [SessionAuthentication, TokenAuthentication]

    def delete(self, request, *args, **kwargs):
        dog_id = kwargs['pk']
        dog = PetName.objects.get(pk=dog_id)
        dog.credentials = None
        dog.save()
        return Response({"message": "Credentials deleted successfully"}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Override the delete method to handle the deletion process
        instance = self.get_object()  # Get the dog instance to be deleted
        #self.perform_destroy(instance)  # Call the method to delete it
        
        instance.delete()
        return Response({"message": "Credentials deleted successfully"}, status=status.HTTP_204_NO_CONTENT)  # Return a no 
        