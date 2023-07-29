from django.urls import path

from . import views

urlpatterns = [
    path('meu_formulario/', views.meu_formulario, name='meu_formulario'),
    path('obter_bancos', views.obter_bancos, name='obter_bancos'),
    
    
]
