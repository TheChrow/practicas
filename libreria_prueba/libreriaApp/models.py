from django.db import models

# Create your models here.
class Autor(models.Model):
    rut = models.CharField(max_length=10)
    nombreAutor = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nombreAutor
    
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    ano = models.DateField()
    genero = models.CharField(max_length=50)
    numeroPaginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)