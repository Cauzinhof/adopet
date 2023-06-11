from rest_framework import serializers
from .models import Tutor, Pet, Abrigo
from .validators import *

class TutorSerializer(serializers.ModelSerializer):
    sobre = serializers.CharField(required=False)

    class Meta:
        model = Tutor
        fields = ['nome', 'email', 'telefone', 'cidade', 'estado', 'sobre']

    def validate(self, attrs):
        if not chars_valido(attrs['nome']):
            raise serializers.ValidationError({'nome':"O nome deve conter apenas letras"})
        if not telefone_valido(attrs['telefone']):
            raise serializers.ValidationError({'telefone':"O telefone deve ser no formato XX XXXXX-XXXX"})
        if not chars_valido(attrs['cidade']):
            raise serializers.ValidationError({'cidade':"A cidade deve conter apenas letras"})
        if not chars_valido(attrs['estado']):
            raise serializers.ValidationError({'estado':"Insira a sigla do estado"})
        return attrs

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ['foto']

    def validate(self, attrs):
        if not chars_valido(attrs['nome']):
            raise serializers.ValidationError({'nome':"O nome deve conter apenas letras"})
        if not chars_valido(attrs['cidade']):
            raise serializers.ValidationError({'cidade':"A cidade deve conter apenas letras"})
        if not chars_valido(attrs['estado']):
            raise serializers.ValidationError({'estado':"Insira a sigla do estado"})
        return attrs

class AbrigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrigo
        fields = '__all__'

    def validate(self, attrs):
        if not chars_valido(attrs['nome']):
            raise serializers.ValidationError({'nome':"O nome deve conter apenas letras"})
        if not chars_valido(attrs['cidade']):
            raise serializers.ValidationError({'cidade':"A cidade deve conter apenas letras"})
        if not chars_valido(attrs['estado']):
            raise serializers.ValidationError({'estado':"Insira a sigla do estado"})
        return attrs