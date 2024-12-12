from django.urls import path

#from .views import cursos, estudiantes, profesores, inicio
from .views import inicio, home, Cursos
from . import views



urlpatterns = [
    path("", inicio, name="Inicio"),
    path("Cursos/", Cursos, name="Cursos"),
    path('home/', views.home, name='home'),
    
    #path("profesores/", profesores, name="Profesores"),

]