from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'marca', 'quantidade_minima', 'quantidade', 'custo', 'preco', 'observacao')


admin.site.register(Produto, ProdutoAdmin)

# Register your models here.
