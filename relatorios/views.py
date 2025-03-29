from django.shortcuts import render
from vendas.models import Venda
from .forms import RelatorioVendaForm

def relatorio_vendas(request):
    form = RelatorioVendaForm(request.GET or None)
    vendas = Venda.objects.none()  # Nenhum dado inicialmente

    if form.is_valid():
        data_inicio = form.cleaned_data['data_inicio']
        data_fim = form.cleaned_data['data_fim']
        vendas = Venda.objects.filter(data_hora__gte=data_inicio, data_hora__lte=data_fim)

    # Garante que sempre há um retorno
    context = {
        'form': form,
        'vendas': vendas,
    }
    return render(request, 'relatorio_vendas.html', context)
