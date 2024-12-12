from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from iades.models import Cursos

# Create your views here.

def inicio(request):

    return render(request, "index.html")

def home(request):

    return render(request, "home.html")
