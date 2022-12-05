"""
Bienvenido al día 91 de #100diasdepython
            El reto de hoy es:
    Crea una funcion que devuelva los cuadrados
de los primeros 10 numeros enteros iniciando en 1
            utilizando yields
        Imprime el resultado en una Lista
"""
def cuadrados(num):
    for i in num:
        yield pow(i,2)

lista = [x for x in cuadrados(range(1,11))]
print (lista)