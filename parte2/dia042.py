"""
    Bienvenido al día 42 de #100diasdepython
            El reto de hoy es:
Utiliza los conjuntos del reto anterior,
define un nuevo conjunto de mascotas,
para encontrar la union de ambos conjuntos
sin usar ciclos e imprime el resultado
"""
animales = {'perro','gallina','paloma','vaca'}
mascotas = {'hamster','perro','canario','loro'}
union = animales.union(mascotas)
print (union)