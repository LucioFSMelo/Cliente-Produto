from django.db import models

class Clientes(models.Model):

    nome = models.CharField(max_length=220)
    cpf = models.IntegerField()
    fone = models.IntegerField()
    email = models.EmailField()
    data_nascimento = models.DateField()
    endereço = models.TextField()
    data_cadastro = models.DateTimeField()
    description = models.TextField()


    def __str__(self):
        return self.nome

