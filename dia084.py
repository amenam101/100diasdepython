"""
Bienvenido al día 84 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para convertir la cadena
        "12-07-2022" a timestamp
            Imprime el resultado
"""
from datetime import datetime
import time

cadena = "12-07-2022"
fecha = datetime.strptime(cadena,"%d-%m-%Y")
ts = time.mktime(fecha.timetuple())
print (ts)