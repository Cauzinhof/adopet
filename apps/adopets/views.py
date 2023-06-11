from .models import Tutor, Pet, Abrigo, Adocao
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import TutorSerializer, PetSerializer, AbrigoSerializer, AdocaoSerializer
# Create your views here.

class TutoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset=Tutor.objects.all()
    serializer_class = TutorSerializer
    
class PetsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pets"""
    queryset=Pet.objects.filter(adotado=False)
    serializer_class = PetSerializer
    #filtro
    #filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    #ordering_fields = ['nome', 'id',]

class AbrigosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os abrigos"""
    queryset=Abrigo.objects.all()
    serializer_class = AbrigoSerializer

class AdocoesViewSet(viewsets.ModelViewSet):
    """Exibindo todas as adoções"""
    queryset=Adocao.objects.all()
    serializer_class = AdocaoSerializer

    def perform_create(self, serializer):
        serializer.save()
        pet = Pet.objects.filter(pk=self.request.POST['animal'])
        pet.update(adotado=True)

    def perform_destroy(self, instance):
        pet_id = instance.animal.id
        pet = Pet.objects.filter(pk=pet_id)
        pet.update(adotado=False)
        instance.delete()
