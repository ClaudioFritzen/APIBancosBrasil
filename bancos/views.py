import requests
from django.shortcuts import render
from django.http import JsonResponse

def obter_bancos(request):
    url = 'https://brasilapi.com.br/api/banks/v1'
    response = requests.get(url)
    bancos_data = response.json()
    return JsonResponse(bancos_data, safe=False)
