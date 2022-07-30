"""
    Bienvenido al día 61 de #100diasdepython
            El reto de hoy es:
Utiliza RegEx para validar que las cadenas de
        la lista sean tiralmente numericas
["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
    Imprime una lista con las cadenas numericas
"""
from re import match

mi_lista = ["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
solo_numeros = list(filter(lambda n: match('^\d+$', n), mi_lista))
print(solo_numeros)
