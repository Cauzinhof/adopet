from .models import BaseUser, Pet, Abrigo, Adocao
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import TutorSerializer, PetSerializer, AbrigoSerializer, AdocaoSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission
# Create your views here.

class TutoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset=BaseUser.objects.filter(eh_tutor=True)
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
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        #Apenas superusuários serão capazes fazer a criação e deleção de abrigos(padrão django)
        tutor = BaseUser.objects.get(pk=self.request.POST['user'])

        #Permissões
        add_adocao = Permission.objects.get(codename='add_adocao')
        change_adocao = Permission.objects.get(codename='change_adocao')
        delete_adocao = Permission.objects.get(codename='delete_adocao')
        add_pet = Permission.objects.get(codename='add_pet')
        change_pet = Permission.objects.get(codename='change_pet')
        delete_pet = Permission.objects.get(codename='delete_pet')

        tutor.user_permissions.add(add_adocao, change_adocao, delete_adocao)
        tutor.user_permissions.add(add_pet, change_pet, delete_pet)

        tutor.eh_tutor = False
        tutor.save()
        serializer.save()

    def perform_destroy(self, instance):
        tutor_id = instance.user.id
        tutor = BaseUser.objects.get(pk=tutor_id)
        tutor.eh_tutor = True
        tutor.save()
        #Ao deletear o abrigo, todas as permissões serão redefinidas
        tutor.user_permissions.clear()
        instance.delete()

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
