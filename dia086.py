"""
Bienvenido al día 86 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para calcular la cantidad
de segundos que han pasado desde el inicio
    del reto considerando solo la fecha
Considera que el reto inicio el "20/04/2022"
            Imprime el resultado
"""
from datetime import datetime

cadena = "20/04/2022"
inicio = datetime.strptime(cadena, '%d/%m/%Y')
hoy = datetime.now()
delta = hoy - inicio
segundos = delta.total_seconds()
print (segundos)