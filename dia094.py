"""
Bienvenido al día 94 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
    para recibir N-cadenas de nombres y
        devuelva una lista de N-saludos
    ejemplo de salida ['Hola Katy', 'Hola Ariel']
        Imprime el resultado en una Lista
"""
def saludo(*nombres):
    lista = [f'Hola {i}' for i in nombres]
    return lista

print (saludo('Katy', 'Ariel'))
