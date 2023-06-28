from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class BaseUser(AbstractUser):

    username = models.CharField(unique=False, max_length=50)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=2, default='MS', blank=False)
    sobre = models.TextField()
    eh_tutor = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objetcts = CustomUserManager()

    def __str__(self) -> str:
        return self.nome

class Pet(models.Model):

    PORTE=[
        ('P', 'Porte pequeno'),
        ('P/M', 'Porte pequeno/médio'),
        ('M', 'Porte médio'),
        ('M/G', 'Porte médio/grande'),
        ('G', 'Porte grande')
    ]

    foto = models.ImageField(upload_to='fotos/pets/', blank=True, default='')
    abrigo = models.ForeignKey(to='Abrigo', on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=20)
    idade = models.CharField(max_length=30)
    porte = models.CharField(max_length=20, choices=PORTE)
    caracteristicas = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2, default='MS')
    adotado = models.BooleanField(default=False)
    tutor = models.ForeignKey(to='BaseUser', on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return f'Pet {self.nome}'

class Abrigo(models.Model):

    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    nome_abrigo = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'Abrigo {self.nome_abrigo}'
    
class Adocao(models.Model):
    animal = models.ForeignKey(to='Pet', on_delete=models.CASCADE)
    tutor = models.ForeignKey(to='BaseUser', on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self) -> str:
        return f'{self.tutor} -> {self.animal}'