import django_filters

from .models import Editorial, Autor, Genero, Libro


class LibroFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(LibroFilter, self).__init__(*args, **kwargs)
        for field_name, field in self.form.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Libro
        fields = ['nombre', 'autor', 'sinopsis', 'rating',
                  'generos', 'editorial', 'ano_publicacion']


class AutorFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(AutorFilter, self).__init__(*args, **kwargs)
        for field_name, field in self.form.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Autor
        fields = ['nombre', 'Apellido', 'fecha_nacimiento', 'biografia']


class EditorialFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(EditorialFilter, self).__init__(*args, **kwargs)
        for field_name, field in self.form.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Editorial
        fields = ['nombre', 'ano', 'historia']


class GeneroFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(GeneroFilter, self).__init__(*args, **kwargs)
        for field_name, field in self.form.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Genero
        fields = ['nombre', 'historia']
