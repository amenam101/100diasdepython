"""
    Bienvenido al día 63 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para validar que las cadenas solo
        contengan caracteres alfanumericos
["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
    Imprime una lista con las cadenas validas
"""
import re

mi_lista = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
patron = "^[a-zA-Z0-9]+$"
validos = [c for c in mi_lista if re.search(patron, c)]
print (validos)