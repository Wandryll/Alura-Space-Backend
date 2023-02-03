from django.db import models
from datetime import datetime
# Create your models here.
class Fotografia(models.Model):

    OPCOES_CATEGORIAS = [
        ("Nebulosa", "Nebulosa"),
        ("Estrela", "Estrela"),
        ("Galáxia", "Galáxia"),
        ("Planeta", "Planeta"),
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime, blank=False)

    def __str__(self) -> str:
        return F"Fotografia [nome={self.nome}]"