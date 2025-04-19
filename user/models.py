from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.username
