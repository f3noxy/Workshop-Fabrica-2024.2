from django.db import models
from Estado.models import EstadoModel

class CidadeModel(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(EstadoModel, on_delete=models.CASCADE, related_name='cidades')

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"