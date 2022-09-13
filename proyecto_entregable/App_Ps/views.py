from django.shortcuts import render
from django.http import HttpResponse
from App_Ps.models import Familia
from django.template import loader

def familia(self):
    familia1 = Familia(nombre = "Johana", edad = 40, fecha_nac = "1982-09-07")
    familia1.save()

    familia2 = Familia(nombre = "Augusto", edad = 47, fecha_nac = "1975-03-15")
    familia2.save()

    familia3 = Familia(nombre = "Sebastian", edad = 22, fecha_nac = "2000-06-27")
    familia3.save()

    diccionario = {
        "name1": familia1.nombre, "age1": familia1.edad, "birth1": familia1.fecha_nac,
        "name2": familia2.nombre, "age2": familia2.edad, "birth2": familia2.fecha_nac,
        "name3": familia3.nombre, "age3": familia3.edad, "birth3": familia3.fecha_nac,
        }
    
    plantilla = loader.get_template("familiar.html")
    document = plantilla.render(diccionario)

    return HttpResponse(document)