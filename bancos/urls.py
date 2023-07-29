from django.urls import path
from . import views

urlpatterns = [
    path('obter_bancos/', views.obter_bancos, name='obter_bancos'),
]
