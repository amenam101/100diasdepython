"""
Bienvenido al día 85 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para imprimir la fecha y
            hora actual en UTC
"""
from datetime import datetime

fecha = datetime.utcnow()
print (fecha)