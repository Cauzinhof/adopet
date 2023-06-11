from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('tutores', views.TutoresViewSet, basename='Tutores')
router.register('pets', views.PetsViewSet, basename='Pets')
router.register('abrigos', views.AbrigosViewSet, basename='Abrigos')
router.register('adocoes', views.AdocoesViewSet, basename='Adoções')

urlpatterns =[
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Para add fotos por meio do gerenciador de arquivos.