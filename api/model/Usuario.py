from django.db import models



class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    nickname = models.CharField(max_length=15, default='@default')
    seguindo = models.TextField(default='')
    seguidores = models.TextField(default='')

    def __str__(self):
        return self.nome
