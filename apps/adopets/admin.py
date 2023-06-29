from django.contrib import admin
from .models import Pet, Adocao, Abrigo, BaseUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class BaseUsers(UserAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    list_display_links = ('id','nome', 'email')
    search_fields = ['nome']
    
admin.site.register(BaseUser, BaseUsers)

class Pets(admin.ModelAdmin):
    list_display = ('id', 'nome', 'abrigo')
    list_display_links = ('id', 'nome')
    search_fields = ['nome', 'abrigo']

admin.site.register(Pet, Pets)

class Adocoes(admin.ModelAdmin):
    list_display = ('id', 'tutor', 'animal')
    list_display_links = ('id', 'tutor', 'animal')
    search_fields = ['tutor', 'animal']

admin.site.register(Adocao, Adocoes)

class Abrigos(admin.ModelAdmin):
    list_display = ('id', 'nome_abrigo')
    list_display_links = ('id', 'nome_abrigo')
    search_fields = ['nome_abrigo']

admin.site.register(Abrigo, Abrigos)