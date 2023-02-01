from django.db import models

# Create your models here.
class Client(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
