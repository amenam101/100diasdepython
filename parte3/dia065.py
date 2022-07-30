"""
    Bienvenido al día 65 de #100diasdepython
                El reto de hoy es:
Utiliza Regex para quitar los prefijos telefonicos de los
            telefonos de la siguiente lista
["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]
Imprime una lista con los telefonos sin prefijos telefonicos
"""
import re

mi_lista = ["+54 11 1234 5678 ", "+591 68754321", "+56 9 8765 4321"]
patron = "\+[1-9]+\s"
remplazo = ""
sin_prefijo = [re.sub(patron,remplazo, i) for i in mi_lista]
print (sin_prefijo)