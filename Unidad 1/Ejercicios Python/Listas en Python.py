"""
LISTAS EN PYTHON

La lista es una colección de datos ordenada, alguna equivalencia con otros lenguajes seria los arrays o vectores. 
La lista puede contener cualquier tipo de dato (enteros, cadenas y otras listas ) veamos como se puede crear una 
lista:"""

lista = ["hola",2,"hacker",[1,2,3,4,5]]

"""si se dan cuenta nuestra lista principal tiene un string "hola", un entero 2 y otra lista, una lista dentro 
de otra lista :) esta definicion estan valida como para python 2.x y 3.x"""

print(lista)
#["hola",2,"hacker",[1,2,3,4,5]]

"""bueno si queremos acceder a uno de los elementos de la lista lo hacemos utilizando el nombre que hacemos
referencia a la lista en este caso lo llame lista puede ser cualquiera y entre corchete indicamos un indice, 
dicho indice va de 0 a n-1 veamos:"""

print(lista[0])
#hola

print(lista[3])
#[1, 2, 3, 4, 5]

"""pero yo quiero es acceder al 2 pero, no se que hago ya que es una lista dentro de otra veamos:"""

print(lista[3][1])
#2

"""wow que bien esto de las tuplas esta muy bien, tenga en cuenta que este operador [] se puede utilizar 
para modificar los elementos de la lista de esta forma:"""

lista[0]= "Python"
print(lista)
#['Phython', 2, 'hacker', [1, 2, 3, 4, 5]]

"""como vimos con el operador [ ] podemos hacer referencia a cualquier elemento de la lista de 0 a n-1 
pero Python trae consigo algo que es recorrer la lista de ultimo al primero utilizando numeros negativos veamos:"""

nombres = ["angelica","paola","hackchan", "python"]

print (nombres[-1])
#python

print (nombres[-4])
#angelica

"""Para los curiosos que no tienen sentido comun ;) eso es bueno cuando se es ultra novatillo es que si haces 
referecia por ejemplo print(nombres[-5]) o print (nombres[4]) va generar un error que dice, lista fuera de 
rango asi:

Traceback (most recent call last):

File "", line 1, in

IndexError: list index out of range"""


"""
SLICING O PARTICIONANDO:


Este mecanismo nos permite seleccionar porciones de listas veamos:

sigamos con esta lista
"""

nombres = ["angelica", "paola", "hackchan", "python"]
print(nombres[1:3])
#['paola', 'hackchan']

"""Como vemos para indicar porciones de lista damos un numero inicial en donde quiero que inicie mi 
porcion seguido de (:) dos puntos y un numero final que me dice el limite de la lista OJO: ese 
numero final actua o me imprime el elemento de la lista contenida en (numerofinal-1) por eso imprime 
hackchan y no Python, si queremos que vaya hasta python solo es:"""

print(nombres[1:4])
#['paola', 'hackchan', 'python']

"""definamos otra lista pero de solo enteros:"""

n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

"""ahora vamos ver que si agregamos un tercer elemento inicio:fin:salto defino un salto para extraer 
los elementos de la lista:

solo con (inicio:fin)
"""

print(n[2:8])
#[ 3, 4, 5, 6, 7, 8 ]

"""ahora con (inicio:fin:salto)"""

print(n[2:8:2])
#[3, 5, 7]

"""Como se dan cuenta con (inicio:fin:salto) lo primero que hace es obtener la lista definida en 
inicio:fin que en este caso al ser de 2:8 nos da [ 3, 4, 5, 6, 7, 8 ] ahora el salto nos dice que 
sea de dos en dos por lo tanto solo va quedar [ 3, 5, 7 ]"""

"""
Extra:

definimos una lista cualquiera o esta :)"""

l=["hackchan",2,"python",7]

print(l[0:]) # imprime desde elemento 0 hasta ?? pues al no indicar nada python lo toma hasta el
             # ultimo
#['hackchan', 2, 'python', 7]

print(l[2:])
#["python", 7 ]

print(l[:3]) #aqui al no indicar inicio pues Python lo toma desde 0
#["hackchan', 2, 'python']

"""Imprimo toda la lista una manera corta de hacerlo con el operador [] :"""

print(l[:])
#['hackchan', 2, 'python', 7]

"""Indico que utlize toda la lista :: y luego a dicha lista muestre los elementos con un salto de dos en 
dos:"""

print(l[::2])
#['hackchan', 'python']

"""tambien podemos modificar los elementos o la fraccion de lista que indicamos asi:"""

l[0:2]=[3,4]

"""ahora impriman la lista y veran lo que paso:"""

print(l)
#[3, 4, 'python', 7]

"""Si ven cambiamos los dos primeros elementos de la lista y eso fue porque l[0:2]=[''hackchan'',2] pues 
eso son los dos elementos que vamos ha cambiar por [3, 4 ] :D bueno espero que me hayan entendido ;) 
bueno esto que hicimos es un manejo a pedal de manejar listas pues python tiene una serie de funciones 
para su tratamiento y que veremos a continuacion para no crear un enredo de temas luego :)

veamos las sigiente funciones basicas para el manejo de listas:


append(object) Añade un objeto al final de la lista

digamos que tenemos:"""

lista=[1,2,3,4,5,6,7]
lista.append(7)
print(lista)
#[1, 2, 3, 4, 5, 6, 7, 7]

"""count(value) devuelve el numero de veces que se encontro value"""

print(lista.count(7))
#2

"""extend([iterable]) añada los elementos del iterable a la lista , hay que tener en cuenta que 
con el lo que hacemos es concatenar dos listas, haber veamos como funciona:"""

lista.extend([8])
#[1, 2, 3, 4, 5, 6, 7, 7,8]

lista.extend([9,10,11,12,13])
#[1, 2, 3, 4, 5, 6, 7, 7,8, 9, 10, 11, 12, 13 ]

print(lista)
#[1, 2, 3, 4, 5, 6, 7, 7,8, 9, 10, 11, 12, 13 ]

"""insert (index, object ) inserta el objeto a la lista en la posicion index veamos:"""

lista.insert(0,10)

print(lista)
#[10, 1, 2, 3, 4, 5, 6, 7, 7,8, 9, 10, 11, 12, 13 ]

"""index( value[, start [, stop ]] ) Devuelve la posicion que encontro la primera ocurrencia de 
value(ya que un valor de una lista puede estar repetido eje: [1,2,2,3] tonces si mando a pedir la 
posicion de 2 index me va a devolver el indice del primer 2 que encuentre en este caso el indice es 
1, si se especifica start y stop que son opcionales indicamos el inicio y el fin de la sublista."""

print(lista.index(10))
#0

"""como ves aun que tenemos dos 10 en la lista uno en la posicion 0 y el otro en la posicion 11 
index me devuelve el indice de la primera coincidencia encontrada en la lista."""

"""pop(index) Devuelve el valor de la posicion index y lo elimina de la lista, si no se especifica 
la posicion, se utiliza el ultimo elemento de la lista"""

lista.pop()
#13

print(lista)
#[10, 1, 2, 3, 4, 5, 6, 7, 7,8, 10, 11, 12 ]

"""remove(value) eliminar la primera ocurrencia de value"""

lista.remove(7)
print(lista)
#[10, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]

lista.remove(10)
print(lista)
#[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]

lista.remove(12)
print(lista)
#[1, 2, 3, 4, 5, 6, 7, 8, 10, 11 ]

""""reverse() invierte la lista. Esta funcion trabaja sobre la propia lista dede la que se invoca 
el metodo, no sobre una copia."""

lista.reverse()
print(lista)
#[11, 10, 8, 7, 6, 5, 4, 3, 2, 1]

"""para dejarla como estaba aplicamos otra ves reverse()"""

lista.reverse()
print(lista)
#[1, 2, 3, 4, 5, 6, 7, 8, 10, 11]