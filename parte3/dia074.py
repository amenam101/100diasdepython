"""
    Bienvenido al día 74 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener el producto
    cartesiano de las siguientes listas
        [1, 3, 5] y [2, 4 ,6]
Imprime el resultado en una lista de tuplas
"""
import itertools

a = [1, 3, 5]
b = [2, 4 ,6]
producto = list(itertools.product(a,b))
print (producto)