
from django.shortcuts import render
from .forms import MeuForm

def meu_formulario(request):
    if request.method == 'POST':
        form = MeuForm(request.POST)
        if form.is_valid():
            # Processar e salvar os dados enviados pelo formulário aqui

            apelido = apelido.POST.get('apelido')
            tipo = tipo.POST.get('tipo')
            valor = valor.POST.get('valor')


            form.save()
            # Por exemplo: apelido = form.cleaned_data['apelido']
            #              banco = form.cleaned_data['banco']
            #              tipo = form.cleaned_data['tipo']
            #              valor = form.cleaned_data['valor']
    else:
        form = MeuForm()
    return render(request, 'meu_formulario.html', {'form': form})


