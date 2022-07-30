"""
Bienvenido al día 26 de #100diasdepython
            El reto de hoy es:
Utiliza la función copy() para crear una
copia de la lista de compras utilizada en
el reto anterior, compara sus ids en memoria
e imprime el resultado
"""
lista_vieja = ["zanahorias","arroz","azucar","huevos","sal","apio"]
lista_nueva =lista_vieja.copy()
print (id(lista_vieja), id(lista_nueva))
