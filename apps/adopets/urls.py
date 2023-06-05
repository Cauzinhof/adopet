from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tutores', views.TutoresViewSet, basename='Tutores')
router.register('pets', views.PetsViewSet, basename='Pets')

urlpatterns =[
    path('', include(router.urls))
]