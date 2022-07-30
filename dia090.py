"""
Bienvenido al día 90 de #100diasdepython
            El reto de hoy es:
    Utiliza datetime para imprimir la fecha y hora
en formato de 12 horas ejemplo "2022/07/18 11:30 PM"
        Imprime el resultado en una cadena
"""
from datetime import datetime
cadena = "2022/07/18 11:30 PM"

fecha12 = datetime.strptime(cadena,"%Y/%m/%d %I:%M %p")
fecha24 = fecha12.strftime("%Y/%m/%d %H:%M %p")
print (fecha24)