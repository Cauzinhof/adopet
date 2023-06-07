from rest_framework import serializers
from .models import Tutor, Pet

class TutorSerializer(serializers.ModelSerializer):
    sobre = serializers.CharField(required=False)
    telefone = serializers.CharField(required=False)
    cidade = serializers.CharField(required=False)

    class Meta:
        model = Tutor
        fields = ['nome', 'email', 'telefone', 'cidade', 'estado', 'sobre']

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

#Apenas um teste