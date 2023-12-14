from django import forms
from .models import Editorial, Autor, Genero, Libro


class LibroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Libro

        fields = ['nombre', 'autor', 'sinopsis', 'rating',
                  'generos', 'editorial', 'portada', 'ano_publicacion']
        RATING = [
            (1, "Mala"),
            (2, "Mediocre"),
            (3, "Buena"),
            (4, "Muy Buena"),
            (5, "Excelente")
        ]
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libro'}),
            'Autores': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Géneros'}),
            'sinopsis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libro'}),
            'rating': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Rating'}),
            'generos': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Géneros'}),
            'editorial': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Editorial'}),
            'ano_publicacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de publicacion'}),
        }

        labels = {
            'name': "",
            'description': ""
        }


class AutorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Autor

        fields = ['nombre', 'Apellido', 'foto',
                  'fecha_nacimiento', 'biografia']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'fecha_nacimiento': forms.DateInput(format='%d/%m/%Y'),
            'biografia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Biografía'}),

        }

        labels = {
            'name': "",
            'description': ""
        }


class EditorialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditorialForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Editorial

        fields = ['nombre', 'ano', 'historia', 'foto']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de fundación'}),
            'historia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Historia'}),
        }

        labels = {
            'name': "",
            'description': ""
        }


class GeneroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Genero

        fields = ['nombre', 'historia', 'foto']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'historia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Historia'}),
        }

        labels = {
            'name': "",
            'description': ""
        }
