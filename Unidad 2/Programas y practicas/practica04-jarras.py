#===============================================
# REPRESENTACIÓN DE ESPACIOS DE ESTADOS
#===============================================
# Recuérdese que según lo que se ha visto en clase, la implementación de la
# representación de un problema de espacio de estados consiste en:

# * Representar estados y acciones mediante una estructura de datos.
# * Definir: estado_inicial, es_estado_final(_), acciones(_), aplica(_,_) y
#   coste_de_aplicar_accion, si el problema tiene coste.

# La siguiente clase Problema representa este esquema general de cualquier
# problema de espacio de estados. Un problema concreto será una subclase de
# Problema, y requerirá implementar acciones, aplica y eventualmente __init__,
# es_estado_final y coste_de_aplicar_accion.

class Problema(object):
    """Clase abstracta para un problema de espacio de estados. Los problemas
    concretos habría que definirlos como subclases de Problema, implementando
    acciones, aplica y eventualmente __init__, es_estado_final y
    coste_de_aplicar_accion. Una vez hecho esto, se han de crear instancias de
    dicha subclase, que serán la entrada a los distintos algoritmos de
    resolución mediante búsqueda."""

    def __init__(self, estado_inicial, estado_final=None):
        """El constructor de la clase especifica el estado inicial y
        puede que un estado_final, si es que es único. Las subclases podrían
        añadir otros argumentos"""

        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def acciones(self, estado):
        """Devuelve las acciones aplicables a un estado dado. Lo normal es
        que aquí se devuelva una lista, pero si hay muchas se podría devolver
        un iterador, ya que sería más eficiente.
        >>> for i in [1, 2, 3]:
        ...     print i,
        ...
        1
        2
        3

        Iterador
        >>> x = iter([1, 2, 3])
        >>> x
        <listiterator object at 0x1004ca850>
        >>> x.next()
        1
        >>> x.next()
        2
        >>> x.next()
        3
        >>> x.next()
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        StopIteration"""
        pass

    def aplica(self, estado, accion):
        """ Devuelve el estado resultante de aplicar accion a estado. Se
        supone que accion es aplicable a estado (es decir, debe ser una de las
        acciones de self.acciones(estado)."""
        pass

    def es_estado_final(self, estado):
        """Devuelve True cuando estado es final. Por defecto, compara con el
        estado final, si éste se hubiera especificado al constructor. Si se da
        el caso de que no hubiera un único estado final, o se definiera
        mediante otro tipo de comprobación, habría que redefinir este método
        en la subclase."""
        return estado == self.estado_final

    def coste_de_aplicar_accion(self, estado, accion):
        """Devuelve el coste de aplicar accion a estado. Por defecto, este
        coste es 1. Reimplementar si el problema define otro coste """
        return 1

# Lo que sigue es un ejemplo de cómo definir un problema como subclase
# de problema. En concreto, el problema de las jarras, visto en clase:

class Jarras(Problema):
    """Problema de las jarras:
    Representaremos los estados como tuplas (x,y) de dos números enteros,
    donde x es el número de litros de la jarra de 4 e y es el número de litros
    de la jarra de 3"""

    def __init__(self):
        super().__init__((0,0))

    def acciones(self,estado):
        print(estado)
        jarra_de_4=estado[0]
        jarra_de_3=estado[1]
        accs=list()
        if jarra_de_4 > 0:
            accs.append("vaciar jarra de 4")
            if jarra_de_3 < 3:
                accs.append("trasvasar de jarra de 4 a jarra de 3")
        if jarra_de_4 < 4:
            accs.append("llenar jarra de 4")
            if jarra_de_3 > 0:
                accs.append("trasvasar de jarra de 3 a jarra de 4")
        if jarra_de_3 > 0:
            accs.append("vaciar jarra de 3")
        if jarra_de_3 < 3:
            accs.append("llenar jarra de 3")
        return accs

    def aplica(self,estado,accion):
        j4=estado[0]
        j3=estado[1]
        if accion=="llenar jarra de 4":
            return (4,j3)
        elif accion=="llenar jarra de 3":
            return (j4,3)
        elif accion=="vaciar jarra de 4":
            return (0,j3)
        elif accion=="vaciar jarra de 3":
            return (j4,0)
        elif accion=="trasvasar de jarra de 4 a jarra de 3":
            return (j4-3+j3,3) if j3+j4 >= 3 else (0,j3+j4)
        else: #  "trasvasar de jarra de 3 a jarra de 4"
            return (j3+j4,0) if j3+j4 <= 4 else (4,j3-4+j4)

    def es_estado_final(self,estado):
        return estado[0]==2

# Ejemplos:
pj = Jarras()
print(pj.estado_inicial)
# (0, 0)
print(pj.acciones(pj.estado_inicial))
# ['llenar jarra de 4', 'llenar jarra de 3']
print(pj.aplica(pj.estado_inicial,"llenar jarra de 4"))
# (4, 0)
print(pj.coste_de_aplicar_accion(pj.estado_inicial,"llenar jarra de 4"))
# 1
print(pj.es_estado_final(pj.estado_inicial))
# False
