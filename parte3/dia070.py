"""
    Bienvenido al día 70 de #100diasdepython
                El reto de hoy es:
Utiliza Regex extraer todas las palabras que
contengan al menos una 'a' en la siguiente cadena
    "Llevas programando 70 dias seguidos"
Imprime una lista con las palabras extraidas
"""
import re

cadena = "Llevas programando 70 dias seguidos"
extraidas = [i for i in cadena.split() if re.search('a', i)]
print (extraidas)