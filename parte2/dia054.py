"""
    Bienvenido al día 54 de #100diasdepython
                El reto de hoy es:
Crea una función que reciba una lista de cadenas y
    devuelva un diccionario con la cantidad
            de vocales de cada cadena
Ejemplo de entrada: ['Python', 'es', 'cool']
Ejemplo de salida: {'Python':1,'es':1,'cool':2}
            Imprime el resultado
"""
def cantidad_vocales(entrada: list) -> dict:
    """Devuelve cada item de una lista con su número de vocales.

    Args:
        entrada (list): Lista de entrada tipo string

    Returns:
        dict: Diccionario que devuelve cada item de la lista con su número de vocales
    """
    salida ={}
    for item in entrada:
        vocales='aeiou'
        num_vocal = 0
        for v in vocales:
            num_vocal += item.lower().count(v)
        salida[item]=num_vocal
    return salida
entrada = ['Python', 'es', 'cool']
print (cantidad_vocales(entrada))