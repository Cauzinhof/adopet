from .models import Tutor, Pet
from rest_framework import viewsets
from .serializer import TutorSerializer, PetSerializer
# Create your views here.

class TutoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset=Tutor.objects.all()
    serializer_class = TutorSerializer
    
class PetsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pets"""
    queryset=Pet.objects.all()
    serializer_class = PetSerializer