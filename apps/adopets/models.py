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

    nome = models.CharField(max_length=20)
    idade = models.CharField(max_length=10)
    porte = models.CharField(max_length=20, choices=PORTE)
    caracteristicas = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)