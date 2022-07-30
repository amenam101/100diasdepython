"""
        Bienvenido al día 69 de #100diasdepython
                El reto de hoy es:
Utiliza Regex extraer todas las 'a' seguidas de
        una o más 'b's de la siguiente cadena
        'abholaaaaabaaabbpythonistaaaaaabbbbb'
Imprime una lista con las subcadenas extraidas
"""
import re

cadena = 'abholaaaaabaaabbpythonistaaaaaabbbbb'
patron = '[a]+[b]'
extraidas = re.findall(patron, cadena)
print (extraidas)