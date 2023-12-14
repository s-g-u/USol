from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Usuario

        fields = ['foto_perfil']

        widgets = {


        }

        labels = {
            'name': "",
            'description': ""
        }


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'first_name', 'last_name']

        widgets = {


        }

        labels = {
            'name': "",
            'description': ""
        }
