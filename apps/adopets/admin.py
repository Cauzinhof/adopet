from django.contrib import admin
from .models import Tutor, Pet
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