from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages

#lietar e cadastrar Clientes

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('cadastrar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})
