from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()


    # def __str__(self):
    #     self.nome    





