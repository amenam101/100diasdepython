"""
    Bienvenido al día 57 de #100diasdepython
            El reto de hoy es:
    Utiliza una funcion lambda para encontrar los
    multiplos de 3 en la lista de numeros
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Imprime el resultado en una nueva lista
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nueva = list(filter(lambda i: i%3==0, numeros))
print(lista_nueva)