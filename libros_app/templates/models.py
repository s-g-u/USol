from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

# Editorial del libro.
class Editorial(models.Model): 
    nombre = models.CharField(verbose_name = "Editorial", max_length = 50)
    año = models.SmallIntegerField(verbose_name = "Año de lanzamiento")
    historia = models.TextField(verbose_name = "Historia") 
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
    
    def __str__(self):
        return self.name
    
    @admin.display(ordering = "Historia")
    def sinopsis(self):
        return format_html(self.description[:150]+"...")   

# Autor del libro.
class Autor(models.Model):  
    nombre = models.CharField(verbose_name = "Nombre", max_length = 50)
    Apellido = models.CharField(verbose_name = "Nombre", max_length = 50)
    año_nacimiento = models.SmallIntegerField(verbose_name = "Año de nacimiento")
    año_defuncion = models.SmallIntegerField(verbose_name = "Año de defunción")
    biografia = models.TextField(verbose_name = "Biografía") 
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return self.name

    @admin.display(ordering = "biografia")
    def sinopsis(self):
        return format_html(self.description[:150]+"...")    

# Género de los libros. 
class Genero(models.Model):  
    nombre = models.CharField(verbose_name = "Género", max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
    
    def __str__(self):
        return self.name

#Libro.
class Libro(models.Model):
    nombre = models.CharField(verbose_name = "Libro", max_length = 100) 
    autor =  models.ManyToManyField(Autor, verbose_name = "Autores", on_delete = models.CASCADE)
    sinopsis = models.TextField(verbose_name = "Sinopsis") 

    RATING = [
        (1, "Malo"),
        (2, "Mediocre"),
        (3, "Bueno"),
        (4, "Muy Bueno"),
        (5, "Excelente"),
    ]

    rating = models.PositiveSmallIntegerField(choices = RATING)
    generos = models.ManyToManyField(Genero, verbose_name = "Géneros")
    editorial = models.ForeignKey(Editorial, verbose_name = "Editorial", on_delete = models.CASCADE)
    portada = models.ImageField(upload_to = "libros", null = True, blank = True, verbose_name = "Portada")
    año = models.SmallIntegerField(verbose_name = "Año de lanzamiento", null = False, blank = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Película"    
        verbose_name_plural = "Películas"    

    def __str__(self):
        return self.name       

    @admin.display(ordering="rating")
    def estrellas(self):
        stars = "*" * self.rating
        return format_html(f"<span style='color:green;'>{stars}</span>")
    
    @admin.display(ordering = "sinopsis")
    def sinopsis(self):
        return format_html(self.description[:150]+"...")    