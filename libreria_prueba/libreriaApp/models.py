from django.db import models
from django.core.exceptions import ValidationError

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

    def clean(self):
        if self.autor.libro_set.count() >= 10:
            raise ValidationError('El autor no puede tener más de 10 libros')