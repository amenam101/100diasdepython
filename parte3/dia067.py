"""
        Bienvenido al día 67 de #100diasdepython
                El reto de hoy es:
Utiliza Regex para cambiar el formato de las fechas
de YYYYMMDD a YYYY-MM-DD de las fechas de la lista
["20221205", "19930612", "20050126", "20211008"]
        Imprime una lista con las fechas
"""
import re

formato_inicial = ["20221205", "19930612", "20050126", "20211008"]
patron = "(\d{4})(\d{2})(\d{2})"
remplazo = "\\1-\\2-\\3"
formato_final = [re.sub(patron,remplazo, i) for i in formato_inicial]
print (formato_final)