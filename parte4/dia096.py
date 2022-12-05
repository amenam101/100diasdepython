"""
        Bienvenido al día 96 de #100diasdepython
                El reto de hoy es:
Crea una funcion que use argumentos arbitrarios de tipo
Keyword para recibir nombre, apellido y edad y devuelva
estos argumentos en un diccionario en el siguiente formato
    {"nombre": "Pepito", "apellido": "Perez", "edad": 25}
            Imprime el resultado
"""
def mifuncion(**kwargs):
    resultado = {"nombre": kwargs["firstname"], "apellido": kwargs["lastname"], "edad": kwargs["age"]}
    return resultado

print(mifuncion(firstname= "Pepito", lastname= "Perez", age = 25))