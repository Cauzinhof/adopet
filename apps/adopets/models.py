from django.db import models

# Create your models here.
class Pet(models.Model):

    PORTE=[
        ('P', 'Porte pequeno'),
        ('P/M', 'Porte pequeno/médio'),
        ('M', 'Porte médio'),
        ('M/G', 'Porte médio/grande'),
        ('G', 'Porte grande')
    ]

    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, default='')
    abrigo = models.ForeignKey(to='Abrigo', on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=20)
    idade = models.CharField(max_length=10)
    porte = models.CharField(max_length=20, choices=PORTE)
    caracteristicas = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    adotado = models.BooleanField(default=False)

class Tutor(models.Model):
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, default='')
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=14)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=2, default='MS', blank=False)
    sobre = models.TextField()

class Abrigo(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=2, default='MS', blank=False)
