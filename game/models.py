from django.db import models


class Aventura(models.Model):
    json = models.JSONField()


class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    ficha = models.JSONField()
    caminho_img = models.CharField(max_length=200, blank=False, null=False)


class Historia(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return self.nome
