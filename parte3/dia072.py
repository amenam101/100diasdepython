"""
    Bienvenido al día 72 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener la cantidad de veces que
se repite cada numero en la lista
        [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
Imprime el resultado en un diccionario con el formato
        {numero:cantidad de repeticiones}
"""
from itertools import takewhile
import itertools

cadena = [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
salida = {}
# valores = list(set(cadena))
# for i in valores:
#     salida[i] = cadena.count(i)
# print(salida)

cadena = sorted (cadena)
for x,y in itertools.groupby(cadena):
    salida[x]= len(list(y))
print (salida)