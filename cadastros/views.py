from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView 
from .models import Cliente
from .models import Endereco
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()

class ClienteCreate(CreateView):
    model = Cliente
    queryset = Cliente.objects.all()
    fields = ['foto','id','nome','sobrenome','cpf','rg','telefone','email']
    success_url = reverse_lazy('cliente_list')

class ClienteUpdate(UpdateView):
    model = Cliente
    queryset = Cliente.objects.all()
    fields = ['foto','id','nome','sobrenome','cpf','rg','telefone','email']
    success_url = reverse_lazy('cliente_list')

class ClienteDelete(DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('cliente_list')

class EnderecoList(ListView):
    model = Endereco
    queryset = Endereco.objects.all()
    def get_queryset(self):
        if self.kwargs.get('cliente_pk'):
            return self.queryset.filter(cliente_id=self.kwargs.get('cliente_pk'))
        return self.queryset.all()
class EnderecoCreate(CreateView):
    model = Endereco
    queryset = Endereco.objects.all()
    fields = ['logradouro','bairro','cidade','estado','numero','email','endereco_principal','descricao','cliente']
    success_url = reverse_lazy('endereco_list')

class EnderecoUpdate(UpdateView):
    model = Endereco

    #def get_object(self, queryset=None):
        #return get_object_or_404(self.model, pk=self.kwargs['pk'])
    fields = ['logradouro','bairro','cidade','estado','numero','email','endereco_principal','descricao','cliente']
    
    def get_success_url(self):
        return reverse_lazy('endereco_cliente',kwargs={'cliente_pk': self.kwargs['pk']})

class EnderecoDelete(DeleteView):
    model = Endereco
    queryset = Endereco.objects.all()
    success_url = reverse_lazy('cliente_list')
