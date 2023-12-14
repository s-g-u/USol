from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages


import django_filters

# Create your views here.

# Importaciones de Modelos

from .models import Editorial, Autor, Genero, Libro


from .forms import LibroForm, AutorForm, EditorialForm, GeneroForm

from .filters import LibroFilter, AutorFilter, EditorialFilter, GeneroFilter


# Importaciones de CBV

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView


from django_filters.views import FilterView


# CLASS BASED VIEWS

class HomeView(TemplateView):
    template_name = "libros_app/inicio.html"


class LibrosList(ListView):
    model = Libro
    template_name = "libros_app/libro/libro_list.html"


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros_app/libro/libro_detail.html"


class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('libros_app:libros')
    template_name = "libros_app/libro/libro_form.html"


class LibroDelete(DeleteView):
    model = Libro
    success_url = reverse_lazy('libros_app:libros')
    template_name = "libros_app/libro/libro_confirm_delete.html"


class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name_suffix = "_update_form"
    template_name = "libros_app/libro/libro_update_form.html"

    def get_success_url(self):
        return reverse_lazy('libros_app:libro_actualizar', args=[self.object.id])+"?ok"


class LibroViewFilter(FilterView):
    model = Libro
    template_name = 'libros_app/libro/libros_filtrar.html'
    paginate_by = 10
    filterset_class = LibroFilter


class AutoresList(ListView):
    model = Autor
    template_name = "libros_app/autor/autor_list.html"


class AutorDetailView(DetailView):
    model = Autor
    template_name = "libros_app/autor/autor_detail.html"


class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('libros_app:autores')
    template_name = "libros_app/autor/autor_form.html"


class AutorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('libros_app:autores')
    template_name = "libros_app/autor/autor_confirm_delete.html"


class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name_suffix = "_update_form"
    template_name = "libros_app/autor/autor_update_form.html"

    def get_success_url(self):
        return reverse_lazy('libros_app:autor_actualizar', args=[self.object.id])+"?ok"


class AutoresViewFilter(FilterView):
    model = Autor
    template_name = 'libros_app/autor/autores_filtrar.html'
    paginate_by = 10
    filterset_class = AutorFilter


class EditorialesList(ListView):
    model = Editorial
    template_name = "libros_app/editorial/editorial_list.html"


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "libros_app/editorial/editorial_detail.html"


class EditorialCreate(CreateView):
    model = Editorial
    form_class = EditorialForm
    success_url = reverse_lazy('libros_app:editoriales')
    template_name = "libros_app/editorial/editorial_form.html"


class EditorialDelete(DeleteView):
    model = Editorial
    success_url = reverse_lazy('libros_app:editoriales')
    template_name = "libros_app/editorial/editorial_confirm_delete.html"


class EditorialUpdate(UpdateView):
    model = Editorial
    form_class = EditorialForm
    template_name_suffix = "_update_form"
    template_name = "libros_app/editorial/editorial_update_form.html"

    def get_success_url(self):
        return reverse_lazy('libros_app:editorial_actualizar', args=[self.object.id])+"?ok"


class EditorialViewFilter(FilterView):
    model = Editorial
    template_name = 'libros_app/editorial/editoriales_filtrar.html'
    paginate_by = 10
    filterset_class = EditorialFilter


class GenerosList(ListView):
    model = Genero
    template_name = "libros_app/genero/genero_list.html"


class GeneroDetailView(DetailView):
    model = Genero
    template_name = "libros_app/genero/genero_detail.html"


class GeneroCreate(CreateView):
    model = Genero
    form_class = GeneroForm
    success_url = reverse_lazy('libros_app:generos')
    template_name = "libros_app/genero/genero_form.html"


class GeneroDelete(DeleteView):
    model = Genero
    success_url = reverse_lazy('libros_app:generos')
    template_name = "libros_app/genero/genero_confirm_delete.html"


class GeneroUpdate(UpdateView):
    model = Genero
    form_class = GeneroForm
    template_name_suffix = "_update_form"
    template_name = "libros_app/genero/genero_update_form.html"

    def get_success_url(self):
        return reverse_lazy('libros_app:genero_actualizar', args=[self.object.id])+"?ok"


class GenerosViewFilter(FilterView):
    model = Genero
    template_name = 'libros_app/genero/generos_filtrar.html'
    paginate_by = 10
    filterset_class = GeneroFilter


class AcercaDeMi(TemplateView):
    template_name = "libros_app/acerca_de_mi.html"
