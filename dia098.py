"""
        Bienvenido al día 98 de #100diasdepython
                El reto de hoy es:
Utiliza timeit para obtener el tiempo de
ejecución de la siguiente función
Imprime el resultado en una sola línea
"""
import timeit

miSetup = "print('Iniciamos...')"

miCodigo = '''
def Lazy():
    suma = 0
    for i in range (0, 50000000):
        suma += i
'''

print (timeit.timeit(stmt=miCodigo, number=1))