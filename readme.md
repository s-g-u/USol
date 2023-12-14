Mi proyecto se llama BookParadise, es una pagina para encontrar toda la informacion necesaria sobre libros.

Mi superusuario es:
user: Sol
password: 1

El objetivo funcional de mi proyecto es tener una pagina web donde uno pueda encontrar informacion sobre libros, editoriales, autores y generos literarios.

La descripcion de los modelos es la siguiente:
El modelo Usuario tiene los atributos: usuario y foto_perfil
El modelo Editorial tiene los atributos: nombre, foto, ano, historia
El modelo Autor tiene los atributos: nombre, Apellido, foto, fecha_nacimiento y biografia
El modelo Genero tiene los atributos: nombre, historia y foto
El modelo Libro tiene los atributos: nombre, autor, sinopsis, rating, generos, editorial, portada y ano_publicacion
El modelo Usuario tiene los atributos: user y foto_de_perfil


IMPORTANTE para correr este programa hay que installar django, django_filters y pillow.
Se compila entrando a la carpeta proyecto_libreria con el comando "python3 manage.py runserver"
