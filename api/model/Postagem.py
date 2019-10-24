from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Postagem(models.Model):
    nome = models.CharField(max_length=20)
    autor = models.CharField(max_length=50, default='default_user')
    data_criada = models.DateTimeField(default=timezone.now)
    texto = models.TextField(default='')
    likes = models.IntegerField(default=0)
    comentarios = models.IntegerField(default=0)
    rts = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
 