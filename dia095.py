"""
Bienvenido al día 95 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
    para recibir N-números y determine en un diccionario
    en el siguiente formato {"mayor": 5, "menor": -10}
        Imprime el resultado
"""
def maxmin(*args):
    mayornum = max(args)
    menornum = min(args)
    resultado = {"mayor": mayornum, "menor": menornum}
    return resultado

print (maxmin(-5, -10, 3, 0, 5, 1, 2))