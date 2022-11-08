from django.db import models

class Director(models.Model):
    name=models.CharField(max_length=40,help_text='Genero de pelicula')

    def __str__(self):
        return self.name


class Pelicula(models.Model):
    titulo=models.CharField(max_length=50)
    #autor=models.ForeignKey('Autor', on_delete=models.SET_NULL,null=True)
    summary=models.TextField(max_length=100,help_text='Ingresa una breve descripcion de la pelicula')
    genero=models.ManyToManyField(Director)

    def __str__(self):
        return self.titulo
