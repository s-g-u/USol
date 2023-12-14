
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages


import django_filters

# Create your views here.

# Importaciones de Modelos

from .forms import UsuarioForm, UserForm
from .models import Usuario


from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Importaciones de CBV

from django.views.generic import UpdateView


class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('usuarios_app:actualizar_usuario', args=[self.object.id])+"?ok"


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name_suffix = "_update_form"

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    def get_success_url(self):
        return reverse_lazy('usuarios_app:actualizar_datos_usuario', args=[self.object.id])+"?ok"


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('libros_app:inicio')

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña inválidos")
        return self.render_to_response(self.get_context_data(form=form))


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('libros_app:inicio')

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))
