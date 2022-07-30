"""
                Bienvenido al día 20 de #100diasdepython
                        El reto de hoy es:
De la siguiente cadena: 'PpYyTtHhOoNnIiSsTtAa'
Separa las mayusculas y las minúsculas sin usar ciclos en nuevas cadenas
e imprime el resultado en una sola línea
"""
cadena='PpYyTtHhOoNnIiSsTtAa'
mayus=cadena[:len(cadena):2]
minus=cadena[1:len(cadena):2]
print(mayus,minus)