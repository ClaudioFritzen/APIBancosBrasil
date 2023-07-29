from django import forms
import requests

class MeuForm(forms.Form):
    apelido = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=10)
    valor = forms.DecimalField(max_digits=10, decimal_places=2)

    def __init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['banco'] = forms.ChoiceField(choices=self.get_bancos())

    # função passando a lista dos bancos
    def get_bancos(self):
        url = 'https://brasilapi.com.br/api/banks/v1'
        response = requests.get(url)
        bancos_data = response.json()
        return [(banco['name'], banco['name']) for banco in bancos_data]
       
        