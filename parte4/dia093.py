"""
Bienvenido al día 93 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use yield y genere los primeros
10 numeros de la serie de Fibonacci
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Imprime el resultado en una lista
"""

def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

lista =list(fib(10))
print (lista)