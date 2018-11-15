from django.db import models

# Create your models here.

class Planeta(models.Model):
    id_swapi = models.IntegerField(null=True)
    nome = models.CharField(max_length=100)
    clima = models.CharField(max_length=100)
    terreno = models.CharField(max_length=100)
    QtdAparicoes = models.IntegerField()

    def __str__(self):
        return self.nome
