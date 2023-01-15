from distutils.command.upload import upload
from random import choices
from django.db import models
from django.contrib.auth.models import User

class Raca(models.Model):
    raça = models.CharField(max_length=50)
    
    def __str__(self):
        return self.raça    

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag    

class Pet(models.Model):
    choices_status = (('P', 'Para Adoção'),
                    ('A', 'Adotado'))
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    tags = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status)
    def __str__(self):
        return self.nome    