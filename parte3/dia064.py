"""
    Bienvenido al día 64 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para quitar los ceros innecesarios
        de las direcciones IP de la lista"
["192.08.001.5", "10.120.023.001", "192.160.2.1"]
    Imprime una lista con las IP validas
"""
import re

mi_lista = ["192.08.001.5", "10.120.023.001", "192.160.2.1"]
patron = "[.][0]+"
remplazo = "."
validos = [re.sub(patron,remplazo, i) for i in mi_lista]
print (validos)