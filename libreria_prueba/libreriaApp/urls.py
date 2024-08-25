from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.libros, name='libros'),
    path('autores/', views.autores, name='autores'),
    path('registrarLibro/', views.registrarLibro, name='registrarLibro'),
    path('registrarAutor/', views.registrarAutor, name='registrarAutor'),
]