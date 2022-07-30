"""
        Bienvenido al día 68 de #100diasdepython
                El reto de hoy es:
Utiliza Regex para cambiar el formato de las fechas
de YYYY-MM-DD a DDMMYYYY a  de las fechas de la lista
["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]
        Imprime una lista con las fechas
"""
import re

formato_inicial = ["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]
patron = "(\d{4})-(\d{2})-(\d{2})"
remplazo = "\\3\\2\\1"
formato_final = [re.sub(patron,remplazo, i) for i in formato_inicial]
print (formato_final)