#!/usr/bin/env python3
"""
Ejercicio 03: Identificación y Clasificación de Objetos Nulos y Especiales

Este script define una función llamada 'NULL_not_found' que tiene como objetivo
identificar y clasificar diferentes tipos de objetos, incluyendo:
- None (objeto nulo).
- NaN (Not a Number, no es un número).
- Booleanos (True/False).
- Enteros con valor cero.
- Cadenas vacías.

La función imprime un mensaje específico que indica el tipo del objeto encontrado
y su valor, junto con su tipo de dato real (clase).
Si el objeto no pertenece a ninguna de las categorías anteriores, imprime
"Type not Found" y devuelve 1. En caso contrario, devuelve 0.

Nombre del archivo: NULL_not_found.py
Funciones permitidas: Ninguna.

Salida esperada al ejecutar tester.py: (Ver enunciado del ejercicio)
"""

# Importa la librería 'math', que proporciona funciones matemáticas.
# En este caso, se utiliza para verificar si un número es NaN (Not a Number).
import math


# Definición de la función 'NULL_not_found'
# 'def' indica que estamos definiendo una función.
# 'NULL_not_found' es el nombre de la función.
# '(object: any)' indica que la función recibe un argumento llamado 'object' que puede ser de cualquier tipo ('any').
# '-> int' especifica que la función debe devolver un valor entero ('int').
def NULL_not_found(object: any) -> int:
    """
    Función que identifica y clasifica diferentes tipos de objetos.

    Esta función evalúa un objeto y determina si pertenece a una de las
    siguientes categorías:
    - None: El objeto es nulo.
    - NaN: El objeto es un número flotante que no representa un número válido.
    - Booleano: El objeto es un valor lógico (True o False).
    - Cero: El objeto es el número entero 0.
    - Cadena vacía: El objeto es una cadena sin caracteres.

    Args:
        object: El objeto a evaluar (puede ser de cualquier tipo).

    Returns:
        int: Devuelve 0 si el objeto pertenece a una de las categorías
             especificadas.
             Devuelve 1 si el objeto no se encuentra entre esas categorias
             e imprime "Type not Found"
    """
    # 1. Comprobar si el objeto es 'None'
    #    'is None' compara si el objeto es exactamente el valor nulo 'None'.
    if object is None:
        # Si el objeto es 'None', se asigna el nombre "Nothing".
        type_name = "Nothing"
    # 2. Comprobar si el objeto es un número flotante 'NaN'
    #    'isinstance(object, float)' comprueba si el objeto es un número flotante.
    #    'math.isnan(object)' comprueba si el objeto flotante es 'NaN'.
    elif isinstance(object, float) and math.isnan(object):
        # Si el objeto es un número flotante 'NaN', se asigna el nombre "Cheese".
        type_name = "Cheese"
    # 3. Comprobar si el objeto es un booleano
    #    'isinstance(object, bool)' comprueba si el objeto es de tipo booleano.
    elif isinstance(object, bool):
        # Si el objeto es un booleano, se asigna el nombre "Fake".
        type_name = "Fake"
    # 4. Comprobar si el objeto es el número cero (0)
    #    'object == 0' compara si el objeto es exactamente igual a 0.
    elif object == 0:
        # Si el objeto es 0, se asigna el nombre "Zero".
        type_name = "Zero"
    # 5. Comprobar si el objeto es una cadena vacía
    #    'object == '' compara si el objeto es una cadena vacía.
    elif object == '':
        # Si el objeto es una cadena vacía, se asigna el nombre "Empty".
        type_name = "Empty"
    # 6. Si no se cumple ninguna de las condiciones anteriores
    else:
        # El objeto no es 'None', 'NaN', booleano, 0 o cadena vacía.
        # Imprimimos "Type not Found" y devolvemos 1
        print("Type not Found")
        return 1
    # 7. Imprimir el nombre del tipo, el objeto y su tipo real
    #    'f"{type_name}: {object} {type(object)}"' es una cadena f-string que permite formatear la salida.
    #    'type(object)' devuelve el tipo de dato del objeto.
    print(f"{type_name}: {object} {type(object)}")
    # 8. Devolver 0 en los casos especificados.
    return 0

'''
# Este es el código de tester.py
from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
'''
