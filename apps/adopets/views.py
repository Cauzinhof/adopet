from django.shortcuts import render
from .models import Tutor, Pet
from rest_framework import viewsets
from .serializer import TutorSerializer, PetSerializer
import requests
# Create your views here.

API_URL = 'http://127.0.0.1:8000/api/'

class TutoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset=Tutor.objects.all()
    serializer_class = TutorSerializer
    
class PetsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pets"""
    queryset=Pet.objects.all()
    serializer_class = PetSerializer

def index(request):
    response = requests.get(API_URL+'tutores')
    data = response.json()
    return render(request, 'adopets/index.html', {'tutores':data})
