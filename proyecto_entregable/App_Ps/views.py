from django.shortcuts import render

from django.http import HttpResponse

from AppFamilia.models import *

from django.template import loader


def familia(self):

    familia1 = Familia(nombre = "Susana", edad = 20, fecha_nac = "2000-5-2")

    familia1.save()

    familia2 = Familia(nombre = "Juan", edad = 10, fecha_nac = "2012-8-12")

    familia2.save()

    familia3 = Familia(nombre = "Maria", edad = 54, fecha_nac = "1968-8-29")

    familia3.save()


    diccionario = {
        "name1": familia1.nombre, "age1": familia1.edad, "birth1": familia1.fecha_nac,
        "name2": familia2.nombre, "age2": familia2.edad, "birth2": familia2.fecha_nac,
        "name3": familia3.nombre, "age3": familia3.edad, "birth3": familia3.fecha_nac
        }

    
    plantilla = loader.get_template("template1.html")

    document = plantilla.render(diccionario)

    return HttpResponse(document)