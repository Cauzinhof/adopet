from django.shortcuts import render
from .models import Tutor, Pet, Abrigo
from rest_framework import viewsets
from .serializer import TutorSerializer, PetSerializer, AbrigoSerializer
import requests
# Create your views here.

class TutoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset=Tutor.objects.all()
    serializer_class = TutorSerializer
    
class PetsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pets"""
    queryset=Pet.objects.all()
    serializer_class = PetSerializer

class AbrigosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os abrigos"""
    queryset=Abrigo.objects.all()
    serializer_class = AbrigoSerializer