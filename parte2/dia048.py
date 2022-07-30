"""
    Bienvenido al día 48 de #100diasdepython
            El reto de hoy es:
Crea un rango de 5 números crea una lista
qye refleje con valores booleanos cuales
    son pares e imprime el resultado
"""
pares = list(range (1,6))
i=0
for numero in pares:
    if numero%2 == 0:
        pares[i]=True
    else:
        pares[i]=False
    i+=1
print (pares)