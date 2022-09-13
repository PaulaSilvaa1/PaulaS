from django.shortcuts import render

from django.http import HttpResponse

from App_Ps.models import *

from django.template import loader


def Familia(self):

    familia1 = Familia(nombre = "Susana", edad = 20, fecha_nac = "2000-5-2")

    familia1.save()

    familia2 = Familia(nombre = "Juan", edad = 10, fecha_nac = "2012-8-12")

    familia2.save()

    familia3 = Familia(nombre = "Maria", edad = 54, fecha_nac = "1968-8-29")

    familia3.save()


    diccionario = {
        "nombre1": familia1.nombre, "edad1": familia1.edad, "f.nacimiento1": familia1.fecha_nac,
        "nombre2": familia2.nombre, "edad2": familia2.edad, "f.nacimiento2": familia2.fecha_nac,
        "nombre3": familia3.nombre, "edad3": familia3.edad, "f.nacimiento3": familia3.fecha_nac
        }

    
    plantilla = loader.get_template("Familiar.html")

    document = plantilla.render(diccionario)

    return HttpResponse(document)