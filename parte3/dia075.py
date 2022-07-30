"""
    Bienvenido al día 75 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener mensaje secreto
en la siguiente cadena "P1y2t3h4o5n6!7"
Imprime el resultado en un cadena
Te dejamos una pista:
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
"""
import itertools

cadena = "P1y2t3h4o5n6!7"
selector = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
resultado = itertools.compress(cadena,selector)
resultado = ''.join(resultado)
print (resultado)