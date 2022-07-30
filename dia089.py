"""
Bienvenido al día 89 de #100diasdepython
            El reto de hoy es:
Utiliza calendar para obtener los dias lunes
        del mes Julio del año 2022
    Imprime el resultado en una lista
"""
import calendar

c = calendar.TextCalendar(calendar.MONDAY)

lista = [i for i in c.itermonthdays(2022,7)]
lunes = [lista[x] for x in range (0,31,7) if x>0 ]

print (lunes)