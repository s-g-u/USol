from django.urls import path, include

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="inicio"),
    path('libro/libros/', LibrosList.as_view(), name="libros"),
    path('libro/libro_agregar/', LibroCreate.as_view(), name="libro_agregar"),
    path('libro/libro_confirm_delete/<int:pk>/',
         LibroDelete.as_view(), name="libro_eliminar"),
    path('libro/libro_actualizar/<int:pk>/',
         LibroUpdate.as_view(), name="libro_actualizar"),
    path('libro/libro_detail/<int:pk>/',
         LibroDetailView.as_view(), name="libro_ver_detalles"),
    path('libro/libros_filtrar', LibroViewFilter.as_view(), name="libros_filtrar"),

    path('autor/autores/', AutoresList.as_view(), name="autores"),
    path('autor/autor_agregar/',  AutorCreate.as_view(), name="autor_agregar"),
    path('autor/autor_confirm_delete/<int:pk>/',
         AutorDelete.as_view(), name="autor_eliminar"),
    path('autor/autor_actualizar/<int:pk>/',
         AutorUpdate.as_view(), name="autor_actualizar"),
    path('autor/autor_detail/<int:pk>/',
         AutorDetailView.as_view(), name="autor_ver_detalles"),
    path('autor/autores_filtrar',
         AutoresViewFilter.as_view(), name="autores_filtrar"),

    path('editorial/editoriales/', EditorialesList.as_view(), name="editoriales"),
    path('editorial/editorial_agregar/',
         EditorialCreate.as_view(), name="editorial_agregar"),
    path('editorial/editorial_confirm_delete/<int:pk>/',
         EditorialDelete.as_view(), name="editorial_eliminar"),
    path('editorial/editorial_actualizar/<int:pk>/',
         EditorialUpdate.as_view(), name="editorial_actualizar"),
    path('editorial/editorial_detail/<int:pk>/',
         EditorialDetailView.as_view(), name="editorial_ver_detalles"),
    path('editorial/editoriales_filtrar',
         EditorialViewFilter.as_view(), name="editoriales_filtrar"),

    path('genero/generos/', GenerosList.as_view(), name="generos"),
    path('genero/genero_agregar/',   GeneroCreate.as_view(), name="genero_agregar"),
    path('genero/genero_confirm_delete/<int:pk>/',
         GeneroDelete.as_view(), name="genero_eliminar"),
    path('genero/genero_actualizar/<int:pk>/',
         GeneroUpdate.as_view(), name="genero_actualizar"),
    path('genero/genero_detail/<int:pk>/',
         GeneroDetailView.as_view(), name="genero_ver_detalles"),
    path('genero/generos_filtrar',
         GenerosViewFilter.as_view(), name="generos_filtrar"),


    path('acerca_de_mi', AcercaDeMi.as_view(), name="acerca_de_mi"),

]
