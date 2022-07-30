"""
    Bienvenido al día 60 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para capitalizar las
        palabras de la siguiente lista
["llevo", "sesenta", "dias", "programando", "wiii"]
    Imprime el resultado en una nueva lista
"""
mi_lista = ["llevo", "sesenta", "dias", "programando", "wiii"]
nueva_lista = list(map(lambda i:i.capitalize(),mi_lista))
print (nueva_lista)