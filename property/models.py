from django.db import models

from user.models import CustomUser

class Imovel(models.Model):
    TIPO_CHOICES = [
        ('apartamento', 'Apartamento'),
        ('casa', 'Casa'),
        ('kitnet', 'Kitnet'),
        ('comercial', 'Comercial'),
    ]

    proprietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='imoveis')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    quartos = models.PositiveIntegerField()
    banheiros = models.PositiveIntegerField()
    vagas_garagem = models.PositiveIntegerField(default=0)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.endereco}"
    

class ContratoLocacao(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('encerrado', 'Encerrado'),
        ('cancelado', 'Cancelado'),
    ]

    locatario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contratos')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='contratos')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ativo')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.imovel.titulo} - {self.locatario.username}"

class Pagamento(models.Model):
    contrato = models.ForeignKey(ContratoLocacao, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.contrato} - {self.valor_pago}"

class Avaliacao(models.Model):
    contrato = models.ForeignKey(ContratoLocacao, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.PositiveIntegerField()
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nota} - {self.usuario.username}"
