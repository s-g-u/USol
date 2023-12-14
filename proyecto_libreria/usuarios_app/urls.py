from django.urls import path, include

from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('usuario_update_form/<int:pk>/',
         UsuarioUpdate.as_view(), name="actualizar_usuario"),
    path('user_update_form/<int:pk>/', UserUpdate.as_view(),
         name="actualizar_datos_usuario"),

    path('login/',  MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="usuarios_app:login"), name="logout"),
    path('signUp/',  SignUp.as_view(), name="signUp"),

]
