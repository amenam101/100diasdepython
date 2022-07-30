"""
    Bienvenido al día 56 de #100diasdepython
            El reto de hoy es:
    Utiliza una funcion lambda para encontrar la raiz
    cuadrada de esta lista de numeros [49, 4, 36, 16, 25]
    Imprime el resultado en una nueva lista
"""
numeros = [49, 4, 36, 16, 25]
lista_nueva = list(map(lambda i: i ** 0.5, numeros))
print(lista_nueva)