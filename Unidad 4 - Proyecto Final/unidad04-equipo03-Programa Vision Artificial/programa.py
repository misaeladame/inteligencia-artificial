"""
Tema 4 - Visión Artificial

Equipo: 3

Nombre: Piña Rosales Cristian Gabriel 
Número de Control: 18130588

Nombre: Adame Sandoval José Misael
Número de Control: 18131209

Nombre: Castro Luna Ricardo Raúl
Número de Control: 18131227

Nombre: Flores Ramos José Luis
Número de Control: 18131237

Nombre: Ruiz Martínez Kevin Alejandro
Número de Control: 18131280
"""

"""
Es un programa realizado en la versión de Python 3.9.2 en el editor de Visual
Studio Code. 

La aplicación desarrollada puedes agregar una imagen depurando desde consola y escogiendo cualquier 
método que constan en cambiar la imagen a diferentes formas.
•	Escala de Grises
•	Máximo Brillo
•	Mínimo Brillo 
•	Negativo de Color 
•	Negativo de Grises 
•	Blanco y Negro

Como utilizar el programa:

Abrir una terminal

PS F:\\Inteligencia Artificial\\Unidad 4\\unidad04-equipo03-Programa Vision Artificial> py
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import programa
>>> programa.escala_de_grises("sixFlags.jpg")
El proceso tardo: 9.29 Segundos
>>> programa.minimo("sixFlags.jpg")
El valor Minimo de grises es:  21
El proceso tardo: 8.52 Segundos
>>> programa.maximo("sixFlags.jpg")
El valor Maximo de grises es:  27
El proceso tardo: 8.83 Segundos
>>> programa.negativo_color("sixFlags.jpg")
El proceso tardo: 8.51 Segundos
>>> programa.blanco_negro("sixFlags.jpg",50) 
El proceso tardo: 8.07 Segundos



Explicación de los comandos utilizados en el programa:

Primero hay que abrir la Terminal y escribir
py
(permite abrir el intérprete de Python)

Luego importamos el archivo (script) con el comando import programa 

Para ejecutar cualquier método es necesario el siguiente comando programa.escala_de_grises("sixFlags.jpg"), 
primero utilizas el nombre del script y después el método a usar recuerda que es necesario agregarle el 
nombre completo con su extensión.

Al ejecutar el comando (y en todos los métodos del programa) abrirá dos ventanas uno con la imagen original 
y la  otra con la imagen cambiada al método que se ejecuto

Otro ejemplo utilizando el comando programa.minimo("sixFlags.jpg")

Utilizando el comando programa.maximo("sixFlags.jpg")

Luego, para el negativo de color programa.negativo_color("sixFlags.jpg")

Finalmente, con el metodo blanco y negro programa.blanco_negro("sixFlags.jpg",50). Este metodo necesita 
su imagen y un numero a degradar la imagen
"""

from PIL import Image
import time

""" ABRIR UNA IMAGEN """
def abrir_imagen(im):
    tiempoIn = time.time()
    ruta = (im)
    im = Image.open(ruta)
    im.show()
    tiempoFin = time.time()
    print('El proceso Tardo:', round(tiempoFin - tiempoIn, 2), 'Segundos')
    
    
"""ESCALA DE GRISES DE LA IMAGEN A COLOR"""
def escala_de_grises(im):
    tiempoIn = time.time()
    ruta = (im)
    im = Image.open(ruta)
    im.show()
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i, j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i, j), pixel)
            j+=1
        i+=1
    im2.show()
    tiempoFin = time.time()
    print('El proceso tardo:', round(tiempoFin - tiempoIn, 2), 'Segundos')
    
    
"""MAXIMO DE GRISES DE LA IMAGEN A COLOR"""
def maximo(im):
    tiempoIn = time.time()
    ruta = (im)
    im = Image.open(ruta)
    im.show()
    im3 = im
    i = 0
    while i < im3.size[0]:
        j = 0
        while j < im3.size[1]:
            maximo = max(im3.getpixel((i, j)))
            pixel = tuple([maximo, maximo, maximo])
            im3.putpixel((i, j), pixel)
            j+=1
        i+=1
    print("El valor Maximo de grises es:", maximo)
    im3.show()
    tiempoFin = time.time()
    print('El proceso tardo:', round(tiempoFin - tiempoIn, 2), 'Segundos')
    
    
"""MINIMO DE GRISES DE LA IMAGEN A COLOR"""
def minimo(im):
    tiempoIn = time.time()
    ruta = (im)
    im = Image.open(ruta)
    im.show()
    im4 = im
    i = 0
    while i < im4.size[0]:
        j = 0 
        while j < im4.size[1]:
            minimo = min(im4.getpixel((i, j)))
            pixel = tuple([minimo, minimo, minimo])
            im4.putpixel((i, j), pixel)
            j+=1
        i+=1
    print("El valor Minimo de grises es:", minimo)
    im4.show() 
    tiempoFin = time.time()
    print('El proceso tardo:', round(tiempoFin - tiempoIn, 2), 'Segundos')


"""NEGATIVO DE LA IMAGEN A COLOR"""
def negativo_color(im):
    tiempoIn = time.time()
    ruta = (im)
    im = Image.open(ruta)
    im.show()
    im5 = im
    i = 0
    while i < im5.size[0]:
        j = 0
        while j < im5.size[1]:
            r, g, b = im5.getpixel((i, j))
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b
            pixel = tuple([rn, gn, bn])
            im5.putpixel((i, j), pixel)
            j+=1
        i+=1
    im5.show()
    tiempoFin = time.time()
    print('El proceso tardo:', round(tiempoFin - tiempoIn, 2), 'Segundos')
   
"""BLANCO Y NEGRO DE LA IMAGEN A COLOR"""
def blanco_negro(im,grisBase):
    tiempoIn = time.time()
    ruta = (im)
    im = Image.open(ruta)
    im.show()
    im6 = im
    i = 0
    while i < im6.size[0]:
        j = 0
        while j < im6.size[1]:
            r, g, b = im6.getpixel((i, j))
            gris = (r + g + b) / 3
            if gris < grisBase:
                im6.putpixel((i, j), (0, 0, 0))
            else:
                im6.putpixel((i, j), (255, 255, 255))   
            j+=1
        i+=1
    im6.show()
    tiempoFin = time.time()
    print('El proceso tardo:', round(tiempoFin - tiempoIn, 2), 'Segundos')