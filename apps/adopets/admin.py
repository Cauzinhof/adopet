from django.contrib import admin
from .models import Tutor, Pet, Adocao, Abrigo
# Register your models here.

class Tutores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cidade')
    list_display_links = ('id', 'nome')
    search_fields = ['nome']

admin.site.register(Tutor, Tutores)

class Pets(admin.ModelAdmin):
    list_display = ('id', 'nome', 'porte')
    list_display_links = ('id', 'nome')
    search_fields = ['nome']

admin.site.register(Pet, Pets)

class Adocoes(admin.ModelAdmin):
    list_display = ('id', 'tutor', 'animal')
    list_display_links = ('id', 'tutor', 'animal')
    search_fields = ['tutor', 'animal']

admin.site.register(Adocao, Adocoes)

class Abrigos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ['nome']

admin.site.register(Abrigo, Abrigos)