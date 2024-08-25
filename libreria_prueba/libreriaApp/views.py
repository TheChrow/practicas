from django.shortcuts import render
from .models import Autor, Libro
from django.core.exceptions import ValidationError

# Create your views here.
def inicio(request):

    libros = Libro.objects.all()

    return render(request, 'libreriaApp/index.html', {'libros': libros})

def libros(self):

    autores = Autor.objects.all()

    return render(self, 'libreriaApp/libros.html', {'autores': autores})

def autores(self):

    return render(self, 'libreriaApp/autores.html')



def registrarLibro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        ano = request.POST['ano']
        genero = request.POST['genero']
        numeroPaginas = request.POST['numeroPaginas']
        autor_id = request.POST['autor']

        mensaje = None
        mensaje2 = None
        mensaje3 = None
        mensaje4 = None
        errorCreacion = None
    

        if not all([titulo, ano, genero, numeroPaginas, autor_id]):
            mensaje = 'Debe completar todos los campos'

        try:
            autor = Autor.objects.get(id=autor_id)
        except Autor.DoesNotExist:
            mensaje2 = 'El autor no existe'

        if autor.libro_set.count() >= 10:
            mensaje3 = 'El autor no puede tener más de 10 libros'

        try:
            libro = Libro(titulo=titulo, ano=ano, genero=genero, numeroPaginas=numeroPaginas, autor_id=autor_id)
            libro.full_clean()
            libro.save()
            mensaje4= 'Libro registrado correctamente'

        except ValidationError as e:
            errorCreacion = e.message_dict
    return render(request, 'libreriaApp/libros.html', {'mensaje': mensaje, 'mensaje2': mensaje2, 'mensaje3': mensaje3, 'mensaje4': mensaje4, 'errorCreacion': errorCreacion})

def registrarAutor(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombreAutor = request.POST['nombreAutor']
        fechaNacimiento = request.POST['fechaNacimiento']
        email = request.POST['email']

        mensaje1 = None
        mensaje2 = None
        mensaje3 = None
        errorCreacion = None

        if not all([rut, nombreAutor, fechaNacimiento, email]):
            mensaje1 = 'Debe completar todos los campos'

        if Autor.objects.filter(rut=rut).exists():
            mensaje2 = 'Ya existe un autor con ese rut'

        try: 
            autor = Autor(rut=rut, nombreAutor=nombreAutor, fechaNacimiento=fechaNacimiento, email=email)
            autor.full_clean()
            autor.save()
            mensaje3 = 'Autor registrado correctamente'
        except ValidationError as e:
            errorCreacion  = e.message_dict
    
    return render(request, 'libreriaApp/autores.html', {'mensaje1': mensaje1, 'mensaje2': mensaje2, 'mensaje3': mensaje3, 'errorCreacion': errorCreacion})