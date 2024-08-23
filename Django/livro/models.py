from django.db import models

class LivroModel(models.Model):
    nome = models.CharField(max_length=255)
    qtd_paginas = models.IntegerField()
    descricao = models.TextField()
    genero = models.CharField(max_length=255)

    def __str__(self):
        return f'O livro {self.nome} foi criado.'