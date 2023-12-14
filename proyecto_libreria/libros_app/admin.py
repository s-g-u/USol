from django.contrib import admin
from .models import Editorial, Autor, Genero, Libro

# Register your models here.

class EditorialAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class AutorAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class GeneroAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class LibroAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display    = ('nombre','get_autores','sinopsis', 'estrellas', 'get_generos', 'editorial', 'ano_publicacion' )


    '''  
  list_display = ('pelicula', 'premiere', 'estrellas', 'sinopsis')
    list_filter = ('genders', 'company', 'premiere')
    ordering = ('premiere',)  ''' 


admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor, AutorAdmin)