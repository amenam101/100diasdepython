"""
    Bienvenido al día 78 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para unir las siguientes
    tuplas (78, 100) ("Dias", "Python")
    Obtiene el tipo de cada dato e
        imprimelo en una lista
"""
import itertools

tupla1 = (78, 100)
tupla2 = ("Dias", "Python")
resultado = [type(k) for k,g  in itertools.groupby(tupla1+tupla2)]
print(resultado)