#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from flask import Flask, render_template, request, redirect, url_for, flash
from urllib.request import urlopen
import json
import urllib.request
import datetime


app = Flask(__name__)
app.secret_key = "mysecretkey"
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lista', methods=['GET', 'POST'])
def lista():
    try:
        nombre_pokemon = request.form.get("nombre_pokemon")
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

        url = "https://pokeapi.co/api/v2/pokemon/" + nombre_pokemon
              
        headers = {'User-Agent': user_agent}

        request2 = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request2)
        buscar_informacion = json.loads(response.read())

        if nombre_pokemon == buscar_informacion['name']:
            nombre = buscar_informacion['name']
            nombre = nombre.capitalize()
            peso = buscar_informacion['weight']
            img = buscar_informacion['sprites']['front_default']
            habilidad = buscar_informacion['abilities'][0]['ability']['name']
            habilidad = habilidad.capitalize()
            altura = buscar_informacion['height']
            url_info = buscar_informacion['species']['url']

            tipo = buscar_informacion['types'][0]['type']['name']
            tipo = tipo.capitalize()

            img = buscar_informacion['sprites']['front_default']  

            estadoFoto = '' 
            if img == None:
                estadoFoto = 'No hay foto'

            return render_template('lista.html', nombre=nombre, p=peso, h=habilidad, a=altura, t=tipo, i=img,estadoFoto=estadoFoto)
        else:
            return render_template('lista.html', nombre=None)
    except:
        return render_template('lista.html', nombre=None)

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)
    
