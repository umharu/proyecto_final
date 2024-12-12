from django.urls import path

#from .views import cursos, estudiantes, profesores, inicio
from .views import inicio, home, Cursos


urlpatterns = [
    path("", inicio, name="Inicio"),
    path("home/", home, name="home"),
    path("Cursos/", Cursos, name="Cursos"),
    #path("profesores/", profesores, name="Profesores"),

]