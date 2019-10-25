from django.db import models
from django.utils import timezone

class Comentario(models.Model):
    autor = models.CharField(max_length=15, default='default_user')
    texto = models.TextField(default='')
    likes = models.IntegerField(default=0)
    data_criada = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.autor

