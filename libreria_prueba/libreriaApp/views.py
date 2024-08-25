from django.shortcuts import render
from .models import Autor, Libro
from django.core.exceptions import ValidationError

# Create your views here.
def inicio(request):
    return render(request, 'libreriaApp/index.html')


def listadoLibros(request):

    pass

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
        return render(request, 'libreriaApp/index.html', {'mensaje': 'Debe completar todos los campos'})

    if Autor.objects.filter(rut=rut).exists():
        return render(request, 'libreriaApp/index.html', {'mensaje': 'Ya existe un autor con ese rut'})

    try: 

        autor = Autor(rut=rut, nombreAutor=nombreAutor, fechaNacimiento=fechaNacimiento, email=email)
        autor.full_clean()
        autor.save()
        return render(request, 'libreriaApp/index.html', {'mensaje': 'Autor registrado correctamente'})    
    except ValidationError as e:
        return render(request, 'libreriaApp/index.html', {'mensaje': e.message_dict})
