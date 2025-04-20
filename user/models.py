from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.TextField()
    imagem_perfil= models.ImageField(upload_to='profile_images/', null=True, blank=True) 
    def __str__(self):
        return self.username
