"""
    Bienvenido al día 50 de #100diasdepython
            El reto de hoy es:
Genera 5 numeros enteros de forma aleatoria
Almacenalos en una lista
Sumalos en imprime el resultado
"""
import random

aleatorios = []
suma = 0
for i in range(5):
    entero = random.randint(1,100)
    aleatorios.append(entero)
    suma += entero
print (aleatorios)
print (suma)