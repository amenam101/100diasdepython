"""
    Bienvenido al día 55 de #100diasdepython
            El reto de hoy es:
    Crea una función recursiva para hacer una
            cuenta regresiva a 0
La funcion tiene como parametro de entrada un numero
    Ejecuta la funcion para el numero 5
Imprime el valor de la cuenta en cada iteracion
"""

def cuenta_regresiva (numero: int) -> int:
    """Funcion que realiza una cuenta regresiva del numero ingresado e imprime cada iteracion.

    Args:
        numero (int): Numero de inicio de la cuenta regresiva.

    Returns:
        int: Imprime la iteración de cada número
    """
    if numero > 0:
        print (numero)
        numero = cuenta_regresiva(numero - 1)
    return numero

print (cuenta_regresiva(5))