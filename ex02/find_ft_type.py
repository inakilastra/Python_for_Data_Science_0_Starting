#!/usr/bin/env python3
"""
Ejercicio 02: Primera función Python

Este script define una función llamada 'all_thing_is_obj' que realiza las siguientes acciones:
1. Recibe un objeto de cualquier tipo como argumento.
2. Imprime un mensaje específico indicando el tipo del objeto recibido.
   Los mensajes varían según el tipo del objeto:
    - Lista: "List : <class 'list'>"
    - Tupla: "Tuple : <class 'tuple'>"
    - Conjunto: "Set : <class 'set'>"
    - Diccionario: "Dict : <class 'dict'>"
    - Cadena "Brian": "Brian is in the kitchen : <class 'str'>"
    - Cadena "Toto": "Toto is in the kitchen : <class 'str'>"
    - Entero: "Type not found"
    - Para cualquier otro tipo no especificado: "Type not found"
3. Devuelve el valor entero 42 en todos los casos.

Nombre del archivo a entregar: find_ft_type.py
Funciones permitidas: Ninguna

Salida esperada al ejecutar tester.py: (ver enunciado del ejercicio)
"""

# Definición de la función 'all_thing_is_obj'
# Utilizamos 'def' para definir una función en Python
# 'all_thing_is_obj' es el nombre de la función
# '(object: any)' define un parámetro llamado 'object' que puede ser de cualquier tipo ('any')
# '-> int' indica que la función debe devolver un valor de tipo entero ('int')
def all_thing_is_obj(object: any) -> int:
    """
    Función que imprime el tipo de objeto y devuelve 42.

    Args:
        object: Objeto de cualquier tipo (lista, tupla, conjunto, diccionario, cadena, entero, etc.).

    Returns:
        int: Siempre devuelve el valor entero 42.
    """

    object_type = type(object)

    if isinstance(object, list):
        print(f"List : {object_type}")
    elif isinstance(object, tuple):
        print(f"Tuple : {object_type}")
    elif isinstance(object, set):
        print(f"Set : {object_type}")
    elif isinstance(object, dict):
        print(f"Dict : {object_type}")
    elif isinstance(object, str):
        print(f"{object} is a string : {object_type}")
    elif isinstance(object, int):
        print("Type not found")
    else:
        print("Type not found")
    return 42
'''    
# Definición de la función 'all_thing_is_obj'
# Utilizamos 'def' para definir una función en Python
# 'all_thing_is_obj' es el nombre de la función
# '(object: any)' define un parámetro llamado 'object' que puede ser de cualquier tipo ('any')
# '-> int' indica que la función debe devolver un valor de tipo entero ('int')
def all_thing_is_obj(object: any) -> int:
    """
    Función que imprime el tipo de objeto y devuelve 42.

    Args:
        object: Objeto de cualquier tipo (lista, tupla, conjunto, diccionario, cadena, entero, etc.).

    Returns:
        int: Siempre devuelve el valor entero 42.
    """
    # 1. Obtener el tipo del objeto recibido como argumento
    #    Usamos la función type(object) para obtener el tipo del objeto
    object_type = type(object)

    # 2. Comprobar el tipo del objeto y mostrar el mensaje correspondiente
    #    Utilizamos estructuras condicionales 'if', 'elif', 'else' para verificar el tipo
    #    La función isinstance(object, tipo) devuelve True si 'object' es del tipo 'tipo', y False en caso contrario

    if isinstance(object, list):
        # Si el objeto es una lista, imprimir "List : <class 'list'>"
        print(f"List : {object_type}")
    elif isinstance(object, tuple):
        # Si el objeto es una tupla, imprimir "Tuple : <class 'tuple'>"
        print(f"Tuple : {object_type}")
    elif isinstance(object, set):
        # Si el objeto es un conjunto, imprimir "Set : <class 'set'>"
        print(f"Set : {object_type}")
    elif isinstance(object, dict):
        # Si el objeto es un diccionario, imprimir "Dict : <class 'dict'>"
        print(f"Dict : {object_type}")
    elif isinstance(object, str):
        # Si el objeto es una cadena de texto
        print(f"{object} is a string : {object_type}") # Mensaje genérico opcional para otras cadenas
    elif isinstance(object, int):
        # Si el objeto es un entero, imprimir "Type not found"
        print("Type not found")
    else:
        # Para cualquier otro tipo de objeto que no hayamos contemplado explícitamente (opcional)
        print("Type not found") # Mensaje genérico para otros tipos no especificados

    # 3. Devolver el valor entero 42 (en todos los casos, independientemente del tipo de objeto)
    return 42
'''

'''    tester.py
import sys
print("Estoy usando Python " + sys.version + "\n")

from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

print(all_thing_is_obj(10))
'''
