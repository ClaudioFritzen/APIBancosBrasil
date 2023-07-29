from django.shortcuts import render, HttpResponse

from .forms import MeuForm

# Create your views here.

def meu_formulario(request):
    if request.method == 'GET':
        return HttpResponse('Olá Mundo!')
    
    elif request.method == 'POST':
        form = MeuForm(request.POST)
        if form.is_valid():
            apelido = apelido.POST.get['apelido']
            # Processar e salvar os dados enviados pelo formulário aqui


            form.save()
            
            # Por exemplo: apelido = form.cleaned_data['apelido']
            #              banco = form.cleaned_data['banco']
            #              tipo = form.cleaned_data['tipo']
            #              valor = form.cleaned_data['valor']

            
    else:
        form = MeuForm()
    return render(request, 'meuapp/meu_formulario.html', {'form': form})



