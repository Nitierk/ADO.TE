from django.db import models

class Raca(models.Model):
    raça = models.CharField(max_length=50)
    
    def __str__(self):
        return self.raca    

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.taga    
