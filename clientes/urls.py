from django.urls import path
from .views import lista_clientes, cadastrar_cliente

urlpatterns = [
    path('', lista_clientes, name='lista_clientes'),
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente')  
]