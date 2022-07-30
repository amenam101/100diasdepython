"""
        Bienvenido al día 66 de #100diasdepython
                El reto de hoy es:
    Utiliza Regex para eliminar los caracteres que
    no sean alfanumericos en las cadenas de la lista
["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
    Imprime una lista con las cadenas limpias
"""
import re

mi_lista = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
patron = "[^a-zA-Z0-9]*"
remplazo = ""
sin_prefijo = [re.sub(patron,remplazo, i) for i in mi_lista]
print (sin_prefijo)