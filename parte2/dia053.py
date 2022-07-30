"""
        Bienvenido al día 53 de #100diasdepython
                El reto de hoy es:
    Crea una función que reciba una lista de
numeros y devuelva una lista de los numeros al cuadrado
    Ejecuta la funcion para la lista [2, 3, 5, 7 ,11]
                Imprime el resultado
"""
def cuadrados (lista: list) -> list:
    """
    Devuelve cada número de una lista al cuadrado.

    Args:
        lista (list): Lista inicial de números
    
    Return:
        list: Lista con cada número al cuadrado
    """
    square = [i**2 for i in lista]
    return square

numeros=[2, 3, 5, 7 ,11]
print (cuadrados(numeros))