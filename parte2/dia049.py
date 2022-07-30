"""
    Bienvenido al día 49 de #100diasdepython
            El reto de hoy es:
Declara una variable numerica con valor 100
Decrementa su valor de 10 en 10 mientras no sea 0
    Imprime el valor de la variable
        en cada iteracion
"""
inicio = 100
for i in range (10):
    if inicio != 0:
        print (inicio)
        inicio -=10
    else:
        break