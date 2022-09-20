from http.client import HTTPResponse
from django.shortcuts import render
from App_Ps.models import Curso, Entregable
from django.http import HttpResponse

def inicio (request):
      return render(request, 'App_Ps/inicio.html')

def estudiantes(request):
      return render(request, 'App_Ps/estudiantes.html')

def profesores(request):
      return render(request, 'App_Ps/profesores.html')

def cursos(request):

      materia= Curso(nombre= 'Hacking', camada=1231)
      materia.save()
      return render(request, 'App_Ps/cursos.html')

def entregables(request):

      ente1= Entregable(nombre= 'Examen 1', fechaEntrega= '2022-09-20')
      ente1.save()
      return render(request, 'App_Ps/entregables.html')