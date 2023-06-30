from .models import BaseUser, Pet, Abrigo, Adocao
from rest_framework import viewsets
from .serializer import TutorSerializer, PetSerializer, AbrigoSerializer, AdocaoSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission

class TutoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset=BaseUser.objects.filter(eh_tutor=True)
    serializer_class = TutorSerializer



class PetsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pets"""
    queryset=Pet.objects.filter(adotado=False)
    serializer_class = PetSerializer

    def perform_create(self, serializer):
        tutor_id = self.request.user.id
        abrigo = Abrigo.objects.get(user=tutor_id)
        serializer.validated_data['abrigo'] = abrigo
        serializer.save()
    
    def perform_destroy(self, instance):

        #Verifica se quem solicitou a alteração é o mesmo usuário que criou o pet
        user_do_abrigo_id = instance.abrigo.user.id
        if not (user_do_abrigo_id == self.request.user.id or self.request.user.is_superuser):
            raise ValidationError("Apenas administrador ou o abrigo que adicionou o pet pode removê-lo")
    
        instance.delete()
    
    def perform_update(self, serializer):
        """Antes do update, verifica se quem solicitou a alteração é o mesmo usuário que criou o pet"""
        user_id = serializer.validated_data['abrigo'].user.id
        if not (user_id == self.request.user.id or self.request.user.is_superuser):
            raise ValidationError("Apenas administrador ou o abrigo que adicionou o pet pode alterá-lo")
        
        serializer.save()

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
        #O abrigo é etirado da lista de tutores
        tutor.eh_tutor = False
        tutor.save()
        serializer.save()

    def perform_destroy(self, instance):
        tutor_id = instance.user.id
        tutor = BaseUser.objects.get(pk=tutor_id)
        #O abrigo retorna para lista de tutores
        tutor.eh_tutor = True
        tutor.save()
        #Ao deletear o abrigo, todas as permissões serão redefinidas
        tutor.user_permissions.clear()
        instance.delete()

class AdocoesViewSet(viewsets.ModelViewSet):
    """Exibindo todas as adoções"""
    queryset=Adocao.objects.all()
    serializer_class = AdocaoSerializer
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        pet = Pet.objects.get(pk=self.request.POST['animal'])
        #Verifica se o pet está no abrigo fazendo a requisição
        if not (pet.abrigo.id == self.request.user or self.request.user.is_superuser):
            raise ValidationError("Apenas administrador ou o abrigo que adicionou o pet pode alterá-lo")

        pet.adotado=True
        pet.save()
        serializer.save()

    def perform_destroy(self, instance):
        user_do_abrigo_id = instance.animal.abrigo.id
        #Verifica se o abrigo responsável pelo pet, ou o admin, está fazendo essa alteração
        if not (user_do_abrigo_id == self.request.user.id or self.request.user.is_superuser):
            raise ValidationError("Apenas administrador ou o abrigo responsável pode fazer essa alteração")
        
        pet_id = instance.animal.id
        pet = Pet.objects.get(pk=pet_id)
        pet.adotado=False
        pet.save()
        instance.delete()
