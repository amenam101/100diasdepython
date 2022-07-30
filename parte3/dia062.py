"""
    Bienvenido al día 62 de #100diasdepython
            El reto de hoy es:
Utiliza RegEx para validar la lista de emails
["pythonlapaz@gmail.com", "dias.com", "comidita@.com", "programando@outlook.com"]
Imprime una lista con los emails validos
"""
import re

correos = ["pythonlapaz@gmail.com", "dias.com", "comidita@.com", "programando@outlook.com"]
patron = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
validos = [c for c in correos if re.search(patron, c)]
print (validos)