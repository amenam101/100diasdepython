"""
Bienvenido al día 92 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use yield y genere la
siguiente serie [1, 2, 3, 2, 1, 2, 3, 2, 1]
    Imprime el resultado en una lista
"""
def serie(num):
    i = 1
    x = 1
    while x<=(num):
        if i<=3:
            yield i
            i+=1
            x+=1
        else:
            yield 2
            i-=3
            x+=1

lista = list(serie(9))
print (lista)