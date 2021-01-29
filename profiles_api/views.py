from django.http import HttpResponse #creando una vista en python
import datetime                      #importar el modulo de Datetime
from django.template import Template,Context,RequestContext
import requests
import json
from django.template.loader import get_template



def saludo (request): # primera vista recibe un request como 
          
    listaPokemones=["spearow","fearow","ekans","arbok","pikachu","raichu",
                    "sandshrew", "sandslash", "nidorina"
                   ]

    listaPokemones2=["spearow","fearow","ekans","arbok","pikachu","raichu",
                    "sandshrew", "sandslash", "nidorina"
                   ]
  
    #  pokemon1="spearow"
    #  pokemon2="fearow"
    #  pokemon3="ekans"
    #  pokemon4="arbok"
    #  pokemon5="pikachu"
    #  pokemon6="raichu"
    #  pokemon7="sandshrew"
    #  pokemon9="sandslash", "nidorina"
                
    doc_externo=get_template('miplantilla.html') #busca la ruta especificada en settings.py template y le agrega esta 
    documento=doc_externo.render({"pokemones":listaPokemones,"pokemones2":listaPokemones2})  #renderizar a este tengo que pasarle directamente el Dic

   
    return HttpResponse(documento)

def despedida(request): #segunda vista 
    return HttpResponse("Hasta luego queridos alumnos")

def damefecha(request):

    fecha_actual=datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,agno,edad):
    
    
    periodo=agno-2021
    edadFutura= edad+periodo
    documento="<html><body><h2> En el año %s tendrás %s años" %(agno,edadFutura)
    return HttpResponse(documento)

def pokemon(request,name):
    
    url='http://pokeapi.co/api/v2/pokemon/%s' %(name)

    
    response = requests.get(url)
    response_json = response.json() # esta variable es un diccionario
    abilities=[]
    skills =  response_json['abilities'] #se toman los valores de la clave abilities

    for ability in skills:
        abilities.append(ability['ability']) 

        print(abilities)

    listaPokemones2=["spearow","fearow","ekans","arbok","pikachu","raichu",
                    "sandshrew", "sandslash", "nidorina"
                   ]
        
    doc_externo=get_template('Habilidades.html') #busca la ruta especificada en settings.py template y le agrega esta 
    documento=doc_externo.render({"list":abilities,"pokemones":listaPokemones2,"pokemon":name})  #renderizar a este tengo que pasarle directamente el Dic

    return HttpResponse(documento)
     
         