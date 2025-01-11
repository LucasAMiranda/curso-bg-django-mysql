from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
#lietar e cadastrar Clientes

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})


def cadastrar_cliente(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        cliente = cliente.objects.filter(cpf=cpf).first()

        if cliente:
            #Atualizar cliente existente
            form = ClienteForm(request.POST, instance=cliente)
        else:
            #Criar novo cliente
            form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm
    
    return render(request, 'cadastrar_cliente.html', {'form':form})

def consultar_cliente():
    try:
        #remove qualquer formatação de cpf antes de buscar 
        cpf = ''.join(filter(str.isdigit, cpf))
        cliente = Cliente.objects.get(cpf=cpf)
        data = {
            'nome': cliente.nome,
            'telefone': cliente.telefone,
            'email': cliente.email
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente não encontrado.'}, status=404)

def excluir_cliente(request, cpf):
    if request.method == 'DELETE':
        try:
            cliente = Cliente.objects.get(cpf=cpf)
            cliente.delete()
            return JsonResponse({'message': 'Cliente excluído com sucesso.'})
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Cliente não econtrado.'}, status=404)
