#!/usr/bin/env python3
"""
Ejercicio 04: Verificador de Paridad

Este script recibe un número como argumento en la línea de comandos,
determina si es par o impar e imprime el resultado.

Si se proporcionan más de un argumento o si el argumento no es un entero,
se lanza una excepción de tipo AssertionError.

Nombre del archivo: whatis.py
Funciones permitidas: Ninguna.

Salida esperada: (Ver enunciado del ejercicio)
"""

import sys

def is_even(number: int) -> str:
    """
    Determina si un número es par o impar.

    Args:
        number (int): El número a evaluar.

    Returns:
        str: "I'm Even." si el número es par, "I'm Odd." si es impar.
    """

    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


if __name__ == "__main__":
  try:

    if len(sys.argv) == 2:
        number = int(sys.argv[1])
        result = is_even(number)
        print(result)
    elif len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
    else:
        print("")
  except ValueError:
      print("AssertionError: argument is not an integer")
  except AssertionError as e:
      print(e)

'''
import sys


def is_even(number: int) -> str:
    """
    Determina si un número es par o impar.

    Args:
        number (int): El número a evaluar.

    Returns:
        str: "I'm Even." si el número es par, "I'm Odd." si es impar.
    """
    # Si el número es divisible por 2 (resto 0), es par.
    if number % 2 == 0:
        return "I'm Even."
    # En caso contrario, es impar.
    else:
        return "I'm Odd."


if __name__ == "__main__":
  try:
    #1. Verificar la cantidad de argumentos.
    #   Si hay 2 argumentos
    if len(sys.argv) == 2:
        # 2. Convertir el argumento a un entero.
        number = int(sys.argv[1])
        # 3. Llamar a la función para determinar si es par o impar.
        result = is_even(number)
        # 4. Imprimir el resultado.
        print(result)
    elif len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
    else:
        print("")
  except ValueError:
      print("AssertionError: argument is not an integer")
  except AssertionError as e:
      print(e)
'''
