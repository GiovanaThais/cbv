from django.contrib import admin
from .models import Cliente
from .models import Endereco


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','foto','nome','sobrenome','cpf','rg','telefone','email']

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['logradouro','bairro','cidade','estado','numero','email','endereco_principal']