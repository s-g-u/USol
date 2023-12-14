from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

# Create your models here.

# Editorial del libro.


class Editorial(models.Model):
    nombre = models.CharField(verbose_name="Editorial", max_length=50)
    foto = models.ImageField(upload_to="editoriales",
                             null=True, blank=True, verbose_name="Editorial")
    ano = models.SmallIntegerField(
        verbose_name="Año de fundacion", blank=True, default=0)
    historia = models.TextField(verbose_name="Historia")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return self.nombre

    @admin.display(ordering="Historia")
    def Historia(self):
        return format_html(self.historia[:150]+"...")

# Autor del libro.


class Autor(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    Apellido = models.CharField(verbose_name="Apellido", max_length=50)
    foto = models.ImageField(
        upload_to="autores", null=True, blank=True, verbose_name="Autor")
    fecha_nacimiento = models.DateField(default=timezone.now)
    biografia = models.TextField(verbose_name="Biografía")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nombre + " " + self.Apellido

    @admin.display(ordering="biografia")
    def sinopsis(self):
        return format_html(self.description[:150]+"...")

# Género de los libros.


class Genero(models.Model):
    nombre = models.CharField(verbose_name="Género", max_length=50)
    historia = models.TextField(verbose_name="Historia", default="")
    foto = models.ImageField(
        upload_to="generos", null=True, blank=True, verbose_name="Género")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

    def __str__(self):
        return self.nombre

# Libro.


class Libro(models.Model):
    nombre = models.CharField(verbose_name="Libro", max_length=100)
    autor = models.ManyToManyField(Autor, verbose_name="Autores")
    sinopsis = models.TextField(verbose_name="sinopsis", blank=True)

    RATING = [
        (1, "Malo"),
        (2, "Mediocre"),
        (3, "Bueno"),
        (4, "Muy Bueno"),
        (5, "Excelente"),
    ]

    rating = models.PositiveSmallIntegerField(choices=RATING)
    generos = models.ManyToManyField(Genero, verbose_name="Géneros")
    editorial = models.ForeignKey(
        Editorial, verbose_name="Editorial", on_delete=models.CASCADE)
    portada = models.ImageField(
        upload_to="libros", null=True, blank=True, verbose_name="Portada")
    ano_publicacion = models.SmallIntegerField(
        verbose_name="Año de publicacion", blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.nombre

    @admin.display(ordering="rating")
    def estrellas(self):
        stars = "*" * self.rating
        return format_html(f"<span style='color:green;'>{stars}</span>")

    @admin.display(ordering="sinopsis")
    def descripcion(self):
        return format_html(self.description[:150]+"...")

    def get_generos(self):
        return ",".join([str(p) for p in self.generos.all()])

    def get_autores(self):
        return ",".join([str(p) for p in self.autor.all()])
