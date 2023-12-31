import requests

from django.shortcuts import render

from django.http import JsonResponse

def obter_bancos(request):
    url = 'https://brasilapi.com.br/api/banks/v1'
    response = response.get(url)
    banco_data = response.json()
    return JsonResponse(banco_data, safe=False)
