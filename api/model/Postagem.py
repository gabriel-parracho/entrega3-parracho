from django.db import models
from django.utils import timezone



class Postagem(models.Model):
    nome = models.CharField(max_length=30)
    autor = models.CharField(max_length=15, default='default_user')
    data_criada = models.DateTimeField(default=timezone.now)
    texto = models.TextField(default='')
    likes = models.IntegerField(default=0)
    comentarios = models.IntegerField(default=0)
    rts = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
 