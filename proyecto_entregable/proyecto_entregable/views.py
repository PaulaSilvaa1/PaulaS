from pipes import Template
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Template, Context
def saludo (request):
    return HttpResponse("<h3>Hola Django - Coder</h3>")

def sumar (request):
    return HttpResponse ("En esta pagina voy a sumar numeros.")

def miNombre(self, nombre):
    texto = f"mi nombre es: {nombre}"
    return HttpResponse(texto)

def probandoTemplate(self):
    miHtml = open("C:/Users/PAULI/OneDrive/Escritorio/Entrega_python/proyecto_entregable/proyecto_entregable/plantilla/template.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento) 