"""
    Bienvenido al día 41 de #100diasdepython
            El reto de hoy es:
Utiliza el conjunto del reto anterior,
define un nuevo conjunto de mascotas,
encuentra su intersección de ambos conjuntos
sin usar ciclos e imprime el resultado
"""
animales = {'perro','gallina','paloma','vaca'}
mascotas = {'hamster','perro','canario','loro'}
interseccion = animales & mascotas
#interseccion = animales.intersection(mascotas)     #Solucion de Python La Paz
print (interseccion)