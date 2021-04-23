from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    foto = models.ImageField()
    nome = models.CharField("nome", max_length=50)
    sobrenome = models.CharField("sobrenome", max_length=100)
    cpf = models.CharField("cpf", max_length=100)
    rg = models.CharField("rg", max_length=80)
    telefone = models.CharField("telefone", max_length=12)
    email = models.EmailField("email")
    begin_date= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table= 'cliente'
        verbose_name = "Cliente" 
        verbose_name_plural = "Clientes"

class Endereco(models.Model):
    
    logradouro = models.CharField("logradouro", max_length=500)
    bairro = models.CharField("bairro", max_length= 100)
    cidade = models.CharField("cidade", max_length=100)
    estado = models.CharField("estado", max_length=100)
    numero = models.CharField("numero", max_length=100)
    email = models.EmailField("email")
    begin_date= models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    endereco_principal = models.BooleanField("Endereço principal", default=False)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name='endereco_cliente',verbose_name='Cliente')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table= 'endereco'
        verbose_name= "Endereço"
        verbose_name_plural= "Endereços"

# Create your models here.
