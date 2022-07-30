"""
    Bienvenido al día 36 de #100diasdepython
            El reto de hoy es:
    Utiliza el diccionario de palabras del reto
anterior para eliminar el primer elemento del
diccionario, imprime la cantidad de elementos
            del diccionario
"""
glosario = {'API': 'Application Programming Interface',
    'bytecode': 'Código intermedio entre el código fuente y el código máquina',
    'IDLE': 'Integrated DeveLopment Environment',
    'módulo': 'Un módulo es un software que agrupa un conjunto de subprogramas y estructuras de datos',
    'tipado débil': 'Característica de un lenguaje de programación que no controla o tiene débiles controles en los tipos de datos en un código de programación',
    'constantes': 'Son los valores que no pueden ser modificados. Pueden ser de cualquier tipo de datos.'
}
primer_key = list(glosario.keys())[0]
glosario.pop(primer_key)
print(len(glosario))

