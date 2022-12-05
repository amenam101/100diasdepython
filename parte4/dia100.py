"""
        Bienvenido al día 100 de #100diasdepython
                El reto de hoy es:
    Utiliza try para capturar e imprimir la excepcion
dentro de la siguiente función y agrega un mensaje
            final utilizando finally
        En este reto si se aceptan multiples print
"""

def dia100():
    mensaje = "Llegaste al último día"
    print(mensaje[len(mensaje)])

try:
    dia100()
except Exception as e:
    print("Error: {}".format(e))
finally:
    print("""Me encantó descubrir nuevas cosas de python a través de estos retos,
100 días se pasaron volando
voy a extrañar este grato hábito mañana :)
Muchas gracias por su esfuerzo con la comunidad!!!""")