"""
    Bienvenido al día 51 de #100diasdepython
            El reto de hoy es:
Crea una función que calcule el volumen de un cilindro
    los parametros de entrada son la base y altura
    El valor de la salida es el volumen del cilindro
Ejecuta la función para el caso base=5, altura=7
            Imprime el resultado
"""
from math import pi

def vol_cilindro(base, altura):
    volumen = pi * ((base/2)**2) * altura
    return volumen

if __name__=='__main__':
    print(vol_cilindro(5,7))
