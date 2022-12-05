"""
    Bienvenido al día 81 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para agregarle a la
        fecha actual 7 dias más
            Imprime el resultado
"""
import datetime

hoy = datetime.date(2022,7,9)
dias = datetime.timedelta(days=7)
fecha = hoy + dias
print (fecha)