from django.db import models

class EstadoModel(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    nacao = models.CharField(max_length=100)
    infoNacao = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.nome