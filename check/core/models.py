from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField()
    limite_compra = models.FloatField()
    observacao = models.TextField()

    def __str__(self):
        return self.nome
