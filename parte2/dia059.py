"""
    Bienvenido al día 59 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para ordenar de forma
ascendente la siguiente lista de tuplas tomando el
        valor numerico como referencia
[("Quimica",88),("Fisica",90),("Lenguaje",97)]
            Imprime el resultado
"""

mi_lista = [("Quimica",88),("Fisica",90),("Lenguaje",97)]
lista_orden = sorted(mi_lista,key=lambda i:i[1])
print (lista_orden)