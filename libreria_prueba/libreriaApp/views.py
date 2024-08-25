from django.shortcuts import render
from .models import Autor, Libro
from django.core.exceptions import ValidationError

# Create your views here.
def inicio(request):

    libros = Libro.objects.all()

    return render(request, 'libreriaApp/index.html', {'libros': libros})

def libros(self):

    return render(self, 'libreriaApp/libros.html')

def autores(self):

    return render(self, 'libreriaApp/autores.html')



def registrarLibro(request):

    titulo = request.POST['titulo']
    ano = request.POST['ano']
    genero = request.POST['genero']
    numeroPaginas = request.POST['numeroPaginas']
    autor = request.POST['autor']

    if not all([titulo, ano, genero, numeroPaginas, autor]):
        return render(request, 'libreriaApp/index.html', {'mensaje': 'Debe completar todos los campos'})
    
    try:
        autor = Autor.objects.get(id=autor)
    except Autor.DoesNotExist:
        return render(request, 'libreriaApp/index.html', {'mensaje': 'El autor no existe'})
    
    try:
        libro = Libro(titulo=titulo, ano=ano, genero=genero, numeroPaginas=numeroPaginas, autor_id=autor)
        libro.full_clean()
        libro.save()
        return render(request, 'libreriaApp/index.html', {'mensaje': 'Libro registrado correctamente'})
    except ValidationError as e:
        return render(request, 'libreriaApp/index.html', {'mensaje': e.message_dict})
    

def registrarAutor(request):

    rut = request.POST['rut']
    nombreAutor = request.POST['nombreAutor']
    fechaNacimiento = request.POST['fechaNacimiento']
    email = request.POST['email']

    if not all([rut, nombreAutor, fechaNacimiento, email]):
        mensaje1 = 'Debe completar todos los campos'
        return render(request, 'libreriaApp/autores.html', {'datosIncompleto':mensaje1}) 

    if Autor.objects.filter(rut=rut).exists():
        mensaje2 = 'Ya existe un autor con ese rut'
        return render(request, 'libreriaApp/autores.html', {'autorexistente': mensaje2})

    try: 
        mensaje3 = 'Autor registrado correctamente'
        autor = Autor(rut=rut, nombreAutor=nombreAutor, fechaNacimiento=fechaNacimiento, email=email)
        autor.full_clean()
        autor.save()
        return render(request, 'libreriaApp/autores.html', {'exitoso': mensaje3})    
    except ValidationError as e:
        return render(request, 'libreriaApp/autores.html', {'errorCreacion': e.message_dict})
