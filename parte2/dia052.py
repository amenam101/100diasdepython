"""
    Bienvenido al día 52 de #100diasdepython
            El reto de hoy es:
Crea una función que convierta un numero entero en binario
            sin usar la funcion bin()
    El parametro de entrada es un numero entero
    El valor de salida es una cadena del valor
            del numero en binario
    Ejecuta la funcion para el numero 52
            Imprime el resultado
"""
def binario (numero):
    base2 = ''
    while numero > 1:
        base2 += ''.join(str(numero%2))
        numero //= 2
    base2 += ''.join(str(numero))
    base2 = base2[::-1]
    return base2

if __name__=='__main__':
    print (binario(52))