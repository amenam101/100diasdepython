"""
            Bienvenido al día 23 de #100diasdepython
                    El reto de hoy es:
Utiliza funciones de cadenas para quitar los
eapacios innecesarios de la siguiente cadena:
"       Python es divertido       "
"""
cadena="       Python es divertido       "
#cadena=cadena.replace("       ","")    # Esta fue mi versión
cadena=cadena.strip()                   # Esta fue la requerida
print(cadena)