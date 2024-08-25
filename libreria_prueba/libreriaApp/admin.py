from django.contrib import admin
from .models import Autor, Libro

class AutorAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombreAutor', 'fechaNacimiento', 'email']
    search_fields = ['rut', 'nombreAutor']
    
class libroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano', 'genero', 'numeroPaginas', 'autor']
    search_fields = ['titulo', 'autor']


# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, libroAdmin)

