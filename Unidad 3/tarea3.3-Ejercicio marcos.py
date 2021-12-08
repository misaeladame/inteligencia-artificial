"""
Tarea 3.3 Ejercicio marcos

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
Ejercicio de Marcos (Frames).

En una biblioteca se quiere implementar un sistema de
recomendación de libros. Para hacer esto se considera el
siguiente conocimiento:

Cada libro tiene un título, una categoría (en este caso, libro de
texto, cuento o novela) y un nivel de enseñanza recomendada
para el lector (todos, infantil, bachillerato o enseñanza
superior). Los libros de ciencia ficción y de aventuras son tipos
de novela. A su vez los libros de texto pueden ser libros de
teoría o libros de ejercicios.

Este sistema debe intentar recomendar lo más adecuado en
cada caso para cada tipo de lector, por tanto, se consideraría lo
siguiente:

En general, cualquier lector que realice una petición, puede
especificar un nivel de enseñanza y una categoría preferida. En
ese caso, se le recomendaría el primer libro existente en la base
de hechos cuya categoría y nivel coincidan con las preferencias
del lector. Si un lector no especifica su nivel de enseñanza se le
recomendaría un libro (de la categoría especificada por el
lector) y que tenga el nivel de todos.

De la misma manera, si se especifica un nivel de enseñanza pero
no la categoría, se le recomendaría el primer libro que se
encuentre en la base de hechos (sin importar la categoría) que
coincida con el nivel especificado. Por último, si el lector no
especifica ni nivel ni categoría preferida, se le recomendaría el
primer libro que se encuentre (sin importar la categoría) y que
tenga el nivel de todos. Una última restricción en el sistema es
que se considera que los cuentos únicamente son adecuados
para los lectores de nivel infantil.

Modelar el sistema anterior completo mediante marcos.
Programarlo en Python.
"""

class LibroFRAME(object):
    def __init__(self):
        self.titulo = TituloSLOT()
        self.categoria = CategoriaSLOT()
        self.nivelEnsenanza = NivelEnsenanzaSLOT()


class TituloSLOT (object):
    def __init__(self):
        self.dominio = LibroFRAME()
        self.rango = "1"
        self.cardinalidad = "1"
        self.valor = ""
        
        
class CategoriaSLOT (object):
    def __init__(self):
        self.dominio = LibroFRAME()
        self.rango = "1"
        self.cardinalidad = "1"
        self.valor = ["Libro de Texto", "Cuento", "Novela"]
        
class NivelEnsenanzaSLOT (object):
    def __init__(self):
        self.dominio = LibroFRAME()
        self.rango = "1"
        self.cardinalidad = "1"
        self.valor = ["Todos", "Infantil", "Bachillerato", "Enseñanza Superior"]