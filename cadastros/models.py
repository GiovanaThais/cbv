from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=80)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    begin_date= models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=True)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table= 'Cliente'

class Endereco(models.Model):
    
    logradouro = models.CharField(max_length=500)
    bairro = models.CharField(max_length= 100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    email = models.EmailField()
    begin_date= models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table= 'Endereco'

# Create your models here.
