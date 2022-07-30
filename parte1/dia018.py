"""
                Bienvenido al día 18 de #100diasdepython
                        El reto de hoy es:
Declara una variable de tipo cadena, encuentra el primer y último carácter
                en orden lexicográficosin usar ciclos e imprímelos
"""
cadena='Python tiene pureza'
cadena=cadena.lower().replace(" ","") #homogenizamos los caracteres, no considero depuración de símbolos
cadena=sorted(cadena) #convertimos en lista y ordenamos
print(cadena[0],cadena[-1]) #imprimimos el primero y el último
